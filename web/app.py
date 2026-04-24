"""
Servidor Web — EducaNorte / Assistente Ribeirinho
Correções: Waitress, rota IA, rota turmas, visual.html, perfil incompleto.
"""

import json, os, sys, socket, hashlib
from datetime import datetime
from flask import Flask, render_template, request, jsonify, session, redirect


_ROOT   = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.abspath(os.path.join(_ROOT, ".."))
_TPL    = os.path.join(_ROOT, "templates")

sys.path.insert(0, _ROOT)
sys.path.insert(0, _PARENT)

from modulo_alfabetizacao.conteudo import LICOES_LEITURA, LICOES_MATEMATICA
from modulo_visual.conteudo_visual import (
    ATIVIDADES_CONTAGEM, ATIVIDADES_IDENTIFICACAO, ATIVIDADES_COMPARACAO
)
from modulo_ambiental.conteudo_ambiental import LICOES_AMBIENTAL
from modulo_saude.conteudo_saude import LICOES_SAUDE
from modulo_cultura.conteudo_cultura import LICOES_CULTURA

# Módulo Infantil — opcional
try:
    from modulo_infantil.conteudo_infantil import MODULOS_INFANTIL
    INFANTIL_OK = True
except ImportError:
    MODULOS_INFANTIL = {}
    INFANTIL_OK = False

try:
    from modulo_fundamental.conteudo_fundamental import MODULOS_FUNDAMENTAL
    FUNDAMENTAL_OK = True
except ImportError:
    MODULOS_FUNDAMENTAL = {}
    FUNDAMENTAL_OK = False

try:
    from modulo_medio.conteudo_medio import MODULOS_MEDIO
    MEDIO_OK = True
except ImportError:
    MODULOS_MEDIO = {}
    MEDIO_OK = False

# IA — opcional, não quebra se não estiver disponível
try:
    from modulo_ia.gerador_ia import gerar_licao_ia, ia_disponivel, chat_ia, modelos_disponiveis
    IA_MODULO_OK = True
except ImportError:
    IA_MODULO_OK = False
    def ia_disponivel(): return False
    def gerar_licao_ia(*a, **k): return None
    def chat_ia(*a, **k): return None
    def modelos_disponiveis(): return []

# ─────────────────────────────────────────────
# Configuração — lida de config.json na raiz
# ─────────────────────────────────────────────

_CONFIG_PATH = os.path.join(_PARENT, "config.json")

def carregar_config():
    """Carrega config.json; cria com valores padrão se não existir."""
    padrao = {
        "senha_professor": "professor123",
        "secret_key": "ribeirinho2025",
        "servidor": {"host": "0.0.0.0", "porta": 5000, "threads": 8},
        "ia": {"modelo": "llama3.2", "url": "http://localhost:11434",
               "timeout_gerar": 90, "timeout_chat": 60}
    }
    if os.path.exists(_CONFIG_PATH):
        try:
            with open(_CONFIG_PATH, encoding="utf-8") as f:
                cfg = json.load(f)
            # Mescla com padrão para garantir todas as chaves
            for k, v in padrao.items():
                if k not in cfg:
                    cfg[k] = v
            return cfg
        except Exception:
            pass
    # Cria o arquivo com valores padrão
    with open(_CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(padrao, f, ensure_ascii=False, indent=2)
    return padrao

CONFIG = carregar_config()

app = Flask(__name__, template_folder=_TPL)
app.secret_key = CONFIG["secret_key"]

ARQUIVO_PERFIS   = os.path.join(_PARENT, "perfis.json")
ARQUIVO_TURMAS   = os.path.join(_PARENT, "turmas.json")
ARQUIVO_AVISOS   = os.path.join(_PARENT, "avisos.json")
ARQUIVO_ATIVIDADES = os.path.join(_PARENT, "atividades.json")

AVATARES = ["🌊", "🐟", "🐬", "🦜", "🌿", "🐊", "⭐", "🌺", "🦋", "🍃"]
MODULOS_TODOS = ["leitura", "matematica", "ambiental", "saude", "cultura"]
MODULOS_INFO  = {
    "leitura":    ("Leitura",       "📖", "#00C9A7", 5),
    "matematica": ("Matemática",    "🔢", "#F4A261", 5),
    "ambiental":  ("Meio Ambiente", "🌿", "#4ADE80", 5),
    "saude":      ("Saúde",         "🏥", "#F87171", 5),
    "cultura":    ("Cultura",       "🎭", "#9B72CF", 5),
}
CORES_TURMA = ["#00C9A7","#F4A261","#9B72CF","#F87171","#FFD166","#4ADE80"]

MODULOS_ENSINO = {
    "infantil":    {"nome": "Infantil",     "icone": "🌱", "cor": "#FFD166", "desc": "Alfabetização inicial · Até 5º ano"},
    "fundamental": {"nome": "Fundamental",  "icone": "📚", "cor": "#00C9A7", "desc": "6º ao 9º ano"},
    "medio":       {"nome": "Médio / Adulto","icone": "🎓", "cor": "#9B72CF", "desc": "1º ao 3º ano do Médio + ENEM"},
}


# ─────────────────────────────────────────────
# Helpers — perfis
# ─────────────────────────────────────────────

def hash_senha(senha):
    """Gera hash SHA-256 da senha."""
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()

def perfil_vazio(nome, avatar="🌊", modulo_ensino="fundamental",
                 nome_completo="", senha_hash=""):
    p = {
        "nome":           nome,           # nome de usuário (login)
        "nome_completo":  nome_completo,  # nome real
        "avatar":         avatar,
        "modulo_ensino":  modulo_ensino,
        "senha_hash":     senha_hash,     # "" = infantil (sem senha)
        "conquistas":     [],
        "sessoes":        [str(datetime.now())],
    }
    for mod in MODULOS_TODOS:
        p[mod] = {"nivel_atual": 1, "acertos_totais": 0, "tentativas_totais": 0}
    return p

def garantir_modulos(p):
    """Garante que todos os módulos existem no perfil — corrige perfis antigos."""
    alterado = False
    for mod in MODULOS_TODOS:
        if mod not in p:
            p[mod] = {"nivel_atual": 1, "acertos_totais": 0, "tentativas_totais": 0}
            alterado = True
    if "modulo_ensino" not in p:
        p["modulo_ensino"] = "fundamental"
        alterado = True
    return alterado

def carregar_perfis():
    if os.path.exists(ARQUIVO_PERFIS):
        with open(ARQUIVO_PERFIS, encoding="utf-8") as f:
            return json.load(f)
    return {}

def _salvar_json(caminho, dados):
    """Salva JSON com segurança: escreve em .tmp e faz rename atômico."""
    tmp = caminho + ".tmp"
    try:
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        os.replace(tmp, caminho)
        return True
    except OSError as e:
        app.logger.error(f"Erro ao salvar {caminho}: {e}")
        return False

def salvar_perfis(perfis):
    _salvar_json(ARQUIVO_PERFIS, perfis)

def perfil_ativo():
    perfis = carregar_perfis()
    return perfis.get(session.get("perfil_ativo"))

def salvar_perfil_ativo(p):
    perfis = carregar_perfis()
    perfis[p["nome"]] = p
    salvar_perfis(perfis)


# ─────────────────────────────────────────────
# Helpers — turmas
# ─────────────────────────────────────────────

def carregar_turmas():
    if os.path.exists(ARQUIVO_TURMAS):
        with open(ARQUIVO_TURMAS, encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_turmas(turmas):
    _salvar_json(ARQUIVO_TURMAS, turmas)

def carregar_avisos():
    if os.path.exists(ARQUIVO_AVISOS):
        with open(ARQUIVO_AVISOS, encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_avisos(avisos):
    _salvar_json(ARQUIVO_AVISOS, avisos)

def carregar_atividades():
    if os.path.exists(ARQUIVO_ATIVIDADES):
        with open(ARQUIVO_ATIVIDADES, encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_atividades(atividades):
    _salvar_json(ARQUIVO_ATIVIDADES, atividades)

def calcular_stats_aluno(p):
    ac = tt = mi = 0
    for chave in MODULOS_TODOS:
        d  = p.get(chave, {})
        ac += d.get("acertos_totais", 0)
        tt += d.get("tentativas_totais", 0)
        if d.get("tentativas_totais", 0) > 0: mi += 1
    return {
        "total_acertos":     ac,
        "total_tentativas":  tt,
        "aproveitamento":    int(ac/tt*100) if tt else 0,
        "modulos_iniciados": mi,
        "conquistas":        len(p.get("conquistas", [])),
        "sessoes":           len(p.get("sessoes", [])),
    }

def stats_turma(turma, perfis):
    alunos = [perfis[a] for a in turma.get("alunos", []) if a in perfis]
    if not alunos:
        return {"total": 0, "media": 0, "acertos": 0}
    stats = [calcular_stats_aluno(a) for a in alunos]
    media = int(sum(s["aproveitamento"] for s in stats) / len(stats))
    acertos = sum(s["total_acertos"] for s in stats)
    return {"total": len(alunos), "media": media, "acertos": acertos}

def gerar_codigo_turma(nome):
    import hashlib
    h = hashlib.md5(nome.encode()).hexdigest()[:4].upper()
    return f"TURMA-{h}"


# ─────────────────────────────────────────────
# Rotas — perfis de aluno
# ─────────────────────────────────────────────

@app.route("/")
def index():
    """Splash — sempre exibe a tela inicial independente de sessão."""
    return render_template("bemvindo.html")

@app.route("/menu")
def menu():
    """Menu do aluno — redireciona para o módulo correto ou para seleção de perfil."""
    perfis = carregar_perfis()
    if "perfil_ativo" not in session or session["perfil_ativo"] not in perfis:
        return redirect("/perfis")
    p = perfil_ativo()
    if garantir_modulos(p):
        salvar_perfil_ativo(p)

    # Redireciona para o menu correto conforme módulo de ensino
    modulo_ensino = p.get("modulo_ensino", "fundamental")
    if modulo_ensino == "infantil":
        return redirect("/infantil")
    if modulo_ensino == "fundamental":
        return redirect("/fundamental")
    if modulo_ensino == "medio":
        return redirect("/medio")

    # Busca avisos e atividades da turma do aluno
    turmas = carregar_turmas()
    nome_aluno  = p["nome"]
    turma_aluno = next((t for t, td in turmas.items() if nome_aluno in td.get("alunos", [])), None)

    todos_avisos = carregar_avisos()
    avisos_visiveis = sorted(
        [a for a in todos_avisos if not a.get("turma") or a.get("turma") == turma_aluno],
        key=lambda a: a.get("data", ""), reverse=True
    )[:3]

    todas_ativ = carregar_atividades()
    atividades_aluno = []
    for at in todas_ativ:
        if at.get("turma") != turma_aluno: continue
        modulo  = at.get("modulo", "")
        nivel_min   = int(at.get("nivel_min", 1))
        nivel_atual = p.get(modulo, {}).get("nivel_atual", 1)
        atividades_aluno.append({**at, "concluida": nivel_atual > nivel_min})

    return render_template("menu.html", progresso=p, hora=datetime.now().hour,
                           avisos=avisos_visiveis,
                           atividades=atividades_aluno,
                           modulos_info=MODULOS_INFO)

@app.route("/infantil")
def infantil():
    p = perfil_ativo()
    if not p: return redirect("/")
    if garantir_modulos(p): salvar_perfil_ativo(p)
    return render_template("infantil_menu.html", progresso=p)

@app.route("/infantil/atividade/<chave>")
def infantil_atividade(chave):
    p = perfil_ativo()
    if not p: return redirect("/")
    if chave not in MODULOS_INFANTIL: return redirect("/infantil")
    mod = MODULOS_INFANTIL[chave]
    nivel = p.get(f"infantil_{chave}", {}).get("nivel", 1)
    nivel = min(nivel, max(mod["atividades"].keys()))
    atividade = mod["atividades"][nivel]
    return render_template("infantil_atividade.html",
                           progresso=p, modulo=mod,
                           atividade=atividade, chave=chave, nivel=nivel)

@app.route("/api/infantil/progresso", methods=["POST"])
def infantil_progresso():
    p = perfil_ativo()
    if not p: return jsonify({"erro": "sem perfil"})
    data    = request.json
    chave   = data.get("chave", "")
    acertos = int(data.get("acertos", 0))
    total   = int(data.get("total", 1))
    if chave not in MODULOS_INFANTIL:
        return jsonify({"erro": "módulo inválido"})
    mod = MODULOS_INFANTIL[chave]
    nivel_max = max(mod["atividades"].keys())
    chave_p = f"infantil_{chave}"
    if chave_p not in p:
        p[chave_p] = {"nivel": 1, "acertos": 0, "tentativas": 0}
    p[chave_p]["acertos"]    += acertos
    p[chave_p]["tentativas"] += total
    avancou = False
    if total > 0 and acertos / total >= 0.7 and p[chave_p]["nivel"] < nivel_max:
        p[chave_p]["nivel"] += 1
        avancou = True
    # Conquistas infantis
    total_ac = sum(p.get(f"infantil_{k}", {}).get("acertos", 0) for k in MODULOS_INFANTIL)
    for qtd, nome_c in [(5,"🌱 Primeiro passo"),(15,"⭐ Aprendiz"),(30,"🔥 Estudioso"),(50,"🏆 Campeão")]:
        if total_ac >= qtd and nome_c not in p.get("conquistas", []):
            p.setdefault("conquistas", []).append(nome_c)
    # Conquistas novas
    novas_conquistas = []
    total_ac = sum(p.get(f"infantil_{k}", {}).get("acertos", 0) for k in MODULOS_INFANTIL)
    for qtd, nome_c in [(5,"🌱 Primeiro passo"),(15,"⭐ Aprendiz"),(30,"🔥 Estudioso"),(50,"🏆 Campeão")]:
        if total_ac >= qtd and nome_c not in p.get("conquistas", []):
            novas_conquistas.append(nome_c)
            p.setdefault("conquistas", []).append(nome_c)
    salvar_perfil_ativo(p)
    return jsonify({"avancou": avancou, "nivel": p[chave_p]["nivel"],
                    "novas_conquistas": novas_conquistas})

# ─────────────────────────────────────────────
# Módulo Fundamental
# ─────────────────────────────────────────────

@app.route("/fundamental")
def fundamental():
    p = perfil_ativo()
    if not p: return redirect("/")
    if garantir_modulos(p): salvar_perfil_ativo(p)
    return render_template("fundamental_menu.html", progresso=p, modulos=MODULOS_FUNDAMENTAL)

@app.route("/fundamental/licao/<chave>")
def fundamental_licao(chave):
    p = perfil_ativo()
    if not p: return redirect("/")
    if chave not in MODULOS_FUNDAMENTAL: return redirect("/fundamental")
    mat = MODULOS_FUNDAMENTAL[chave]
    chave_p = f"fund_{chave}"
    nivel = p.get(chave_p, {}).get("nivel_atual", 1)
    nivel = min(nivel, max(mat["licoes"].keys()))
    licao = mat["licoes"][nivel]
    return render_template("fundamental_licao.html",
                           progresso=p, materia=mat,
                           licao=licao, chave=chave, nivel=nivel)

@app.route("/api/fundamental/progresso", methods=["POST"])
def fundamental_progresso():
    p = perfil_ativo()
    if not p: return jsonify({"erro": "sem perfil"})
    data    = request.json
    chave   = data.get("chave", "")
    nivel   = int(data.get("nivel", 1))
    acertos = int(data.get("acertos", 0))
    total   = int(data.get("total", 1))
    if chave not in MODULOS_FUNDAMENTAL:
        return jsonify({"erro": "módulo inválido"})
    mat       = MODULOS_FUNDAMENTAL[chave]
    nivel_max = max(mat["licoes"].keys())
    chave_p   = f"fund_{chave}"
    if chave_p not in p:
        p[chave_p] = {"nivel_atual": 1, "acertos_totais": 0, "tentativas_totais": 0}
    p[chave_p]["acertos_totais"]    += acertos
    p[chave_p]["tentativas_totais"] += total
    avancou = False
    if total > 0 and acertos / total >= 0.7 and nivel < nivel_max:
        p[chave_p]["nivel_atual"] = nivel + 1
        avancou = True
    # Conquistas
    total_ac = sum(p.get(f"fund_{k}", {}).get("acertos_totais", 0) for k in MODULOS_FUNDAMENTAL)
    for qtd, nome_c in [(10,"📖 Leitor iniciante"),(30,"⭐ Estudante dedicado"),(60,"🔥 Saber em chamas"),(100,"🏆 Mestre do saber")]:
        if total_ac >= qtd and nome_c not in p.get("conquistas", []):
            p.setdefault("conquistas", []).append(nome_c)
    salvar_perfil_ativo(p)
    return jsonify({"avancou": avancou, "nivel": p[chave_p]["nivel_atual"]})

# ─────────────────────────────────────────────
# Módulo Médio / Adulto
# ─────────────────────────────────────────────

@app.route("/medio")
def medio():
    p = perfil_ativo()
    if not p: return redirect("/")
    if garantir_modulos(p): salvar_perfil_ativo(p)
    return render_template("medio_menu.html", progresso=p, modulos=MODULOS_MEDIO)

@app.route("/medio/licao/<chave>")
def medio_licao(chave):
    p = perfil_ativo()
    if not p: return redirect("/")
    if chave not in MODULOS_MEDIO: return redirect("/medio")
    mat    = MODULOS_MEDIO[chave]
    chave_p = f"medio_{chave}"
    nivel  = p.get(chave_p, {}).get("nivel_atual", 1)
    nivel  = min(nivel, max(mat["licoes"].keys()))
    licao  = mat["licoes"][nivel]
    return render_template("medio_licao.html",
                           progresso=p, materia=mat,
                           licao=licao, chave=chave, nivel=nivel)

@app.route("/api/medio/progresso", methods=["POST"])
def medio_progresso():
    p = perfil_ativo()
    if not p: return jsonify({"erro": "sem perfil"})
    data    = request.json
    chave   = data.get("chave", "")
    nivel   = int(data.get("nivel", 1))
    acertos = int(data.get("acertos", 0))
    total   = int(data.get("total", 1))
    if chave not in MODULOS_MEDIO:
        return jsonify({"erro": "módulo inválido"})
    mat       = MODULOS_MEDIO[chave]
    nivel_max = max(mat["licoes"].keys())
    chave_p   = f"medio_{chave}"
    if chave_p not in p:
        p[chave_p] = {"nivel_atual": 1, "acertos_totais": 0, "tentativas_totais": 0}
    p[chave_p]["acertos_totais"]    += acertos
    p[chave_p]["tentativas_totais"] += total
    avancou = False
    if total > 0 and acertos / total >= 0.7 and nivel < nivel_max:
        p[chave_p]["nivel_atual"] = nivel + 1
        avancou = True
    # Conquistas do módulo médio
    total_ac = sum(p.get(f"medio_{k}", {}).get("acertos_totais", 0) for k in MODULOS_MEDIO)
    for qtd, nome_c in [
        (10,  "📚 Primeiro passo"),
        (35,  "⭐ Estudante de Ensino Médio"),
        (70,  "🔥 Vestibulando"),
        (120, "🎓 Preparado para o ENEM"),
        (200, "🏆 Mestre do conhecimento"),
    ]:
        if total_ac >= qtd and nome_c not in p.get("conquistas", []):
            p.setdefault("conquistas", []).append(nome_c)
    salvar_perfil_ativo(p)
    return jsonify({"avancou": avancou, "nivel": p[chave_p]["nivel_atual"]})

@app.route("/perfis")
def ver_perfis():
    return render_template("perfis.html", perfis=carregar_perfis(),
                           avatares=AVATARES, modulos_ensino=MODULOS_ENSINO)

@app.route("/selecionar/<nome>")
def selecionar_perfil(nome):
    perfis = carregar_perfis()
    if nome in perfis:
        session["perfil_ativo"] = nome
        perfis[nome]["sessoes"].append(str(datetime.now()))
        salvar_perfis(perfis)
    return redirect("/menu")

@app.route("/escolher-modulo")
def escolher_modulo():
    """Tela de escolha do módulo após clicar em Começar."""
    return render_template("escolher_modulo.html", modulos_ensino=MODULOS_ENSINO)

@app.route("/infantil-direto", methods=["GET", "POST"])
def infantil_direto():
    """Módulo infantil — entrada direta com nome simples, sem senha."""
    erro = None
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        if not nome:
            erro = "Digite seu nome para continuar."
        else:
            perfis = carregar_perfis()
            if nome not in perfis:
                perfis[nome] = perfil_vazio(nome, "🌊", "infantil",
                                            nome_completo=nome, senha_hash="")
                salvar_perfis(perfis)
            else:
                # Perfil infantil existente — atualiza sessão
                perfis[nome]["sessoes"].append(str(datetime.now()))
                salvar_perfis(perfis)
            session["perfil_ativo"] = nome
            return redirect("/menu")
    return render_template("infantil_direto.html", erro=erro)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Login para módulos Fundamental e Médio."""
    modulo = request.args.get("modulo", request.form.get("modulo", "fundamental"))
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        senha   = request.form.get("senha", "").strip()
        if not usuario or not senha:
            return render_template("login_cadastro.html", modulo=modulo,
                                   modulos_ensino=MODULOS_ENSINO, erro="Preencha todos os campos.")
        perfis = carregar_perfis()
        if usuario not in perfis:
            return render_template("login_cadastro.html", modulo=modulo,
                                   modulos_ensino=MODULOS_ENSINO, erro="Usuário não encontrado.")
        p = perfis[usuario]
        if p.get("senha_hash", "") != hash_senha(senha):
            return render_template("login_cadastro.html", modulo=modulo,
                                   modulos_ensino=MODULOS_ENSINO, erro="Senha incorreta.")
        session["perfil_ativo"] = usuario
        perfis[usuario]["sessoes"].append(str(datetime.now()))
        salvar_perfis(perfis)
        return redirect("/menu")
    return render_template("login_cadastro.html", modulo=modulo,
                           modulos_ensino=MODULOS_ENSINO, erro=None)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome_completo = request.form.get("nome_completo", "").strip()
    usuario       = request.form.get("usuario", "").strip().lower()
    senha         = request.form.get("senha", "").strip()
    modulo_ensino = request.form.get("modulo_ensino", "fundamental")

    # Infantil — sem senha, nome simples
    if modulo_ensino == "infantil":
        nome = request.form.get("nome", "").strip() or nome_completo
        if not nome: return redirect("/escolher-modulo")
        perfis = carregar_perfis()
        if nome not in perfis:
            perfis[nome] = perfil_vazio(nome, "🌊", "infantil",
                                        nome_completo=nome, senha_hash="")
            salvar_perfis(perfis)
        session["perfil_ativo"] = nome
        return redirect("/menu")

    # Fundamental / Médio — com senha
    perfis = carregar_perfis()
    erro = None
    if not nome_completo: erro = "Digite seu nome completo."
    elif not usuario:     erro = "Escolha um nome de usuário."
    elif not senha:       erro = "Escolha uma senha."
    elif len(senha) < 4:  erro = "A senha deve ter pelo menos 4 caracteres."
    elif usuario in perfis: erro = "Esse nome de usuário já existe. Escolha outro."

    if erro:
        return render_template("login_cadastro.html", modulo=modulo_ensino,
                               modulos_ensino=MODULOS_ENSINO, erro=erro, modo="cadastro",
                               form_data={"nome_completo": nome_completo, "usuario": usuario})

    perfis[usuario] = perfil_vazio(usuario, "🌊", modulo_ensino,
                                   nome_completo=nome_completo,
                                   senha_hash=hash_senha(senha))
    salvar_perfis(perfis)
    session["perfil_ativo"] = usuario
    return redirect("/menu")

@app.route("/sair")
def sair():
    session.pop("perfil_ativo", None)
    return redirect("/")

@app.route("/excluir/<nome>", methods=["POST"])
def excluir_perfil(nome):
    perfis = carregar_perfis()
    if nome in perfis:
        del perfis[nome]
        salvar_perfis(perfis)
    if session.get("perfil_ativo") == nome:
        session.pop("perfil_ativo", None)
    return redirect("/perfis")


# ─────────────────────────────────────────────
# Rotas — módulos de lição
# ─────────────────────────────────────────────

MAPA_LICOES = {
    "leitura":    LICOES_LEITURA,
    "matematica": LICOES_MATEMATICA,
    "ambiental":  LICOES_AMBIENTAL,
    "saude":      LICOES_SAUDE,
    "cultura":    LICOES_CULTURA,
}

@app.route("/licao/<area>")
def licao(area):
    p = perfil_ativo()
    if not p: return redirect("/")
    if area not in MAPA_LICOES: return redirect("/")
    garantir_modulos(p)
    nivel       = p[area]["nivel_atual"]
    licao_atual = MAPA_LICOES[area].get(nivel, {})
    return render_template("licao.html", area=area, nivel=nivel,
                           licao=licao_atual, progresso=p)

@app.route("/visual")
def visual():
    p = perfil_ativo()
    if not p: return redirect("/")
    return render_template("visual.html", progresso=p,
                           contagem=ATIVIDADES_CONTAGEM,
                           identificacao=ATIVIDADES_IDENTIFICACAO,
                           comparacao=ATIVIDADES_COMPARACAO)

@app.route("/progresso")
def progresso():
    p = perfil_ativo()
    if not p: return redirect("/")
    if garantir_modulos(p): salvar_perfil_ativo(p)
    modulo_ensino = p.get("modulo_ensino", "fundamental")
    return render_template("progresso.html", progresso=p,
                           modulo_ensino=modulo_ensino,
                           modulos_fundamental=MODULOS_FUNDAMENTAL,
                           modulos_medio=MODULOS_MEDIO,
                           modulos_infantil=MODULOS_INFANTIL)


# ─────────────────────────────────────────────
# API — lições
# ─────────────────────────────────────────────

@app.route("/api/responder", methods=["POST"])
def responder():
    data     = request.json
    area     = data.get("area")
    nivel    = int(data.get("nivel", 1))
    idx      = int(data.get("indice", 0))
    resposta = data.get("resposta", "").strip()
    licoes   = MAPA_LICOES.get(area, LICOES_LEITURA)
    perguntas = licoes.get(nivel, {}).get("perguntas", [])
    if idx >= len(perguntas):
        return jsonify({"erro": "índice inválido"})
    p_atual = perguntas[idx]
    correta = resposta.lower() == p_atual["resposta"].lower()
    return jsonify({
        "correta":        correta,
        "resposta_certa": p_atual["resposta"],
        "dica":           p_atual["dica"],
        "ultima":         idx >= len(perguntas) - 1,
    })

@app.route("/api/finalizar", methods=["POST"])
def finalizar():
    data    = request.json
    area    = data.get("area")
    acertos = int(data.get("acertos", 0))
    total   = int(data.get("total", 0))
    nivel   = int(data.get("nivel", 1))
    p = perfil_ativo()
    if not p: return jsonify({"erro": "sem perfil"})
    garantir_modulos(p)
    nivel_max = max(MAPA_LICOES.get(area, LICOES_LEITURA).keys())
    p[area]["acertos_totais"]    += acertos
    p[area]["tentativas_totais"] += total
    avancou = False
    if total > 0 and acertos / total >= 0.7 and nivel < nivel_max:
        p[area]["nivel_atual"] = nivel + 1
        avancou = True
    # Conquistas
    novas = []
    total_ac = sum(p.get(a, {}).get("acertos_totais", 0) for a in MODULOS_TODOS)
    for qtd, nome_c in [(10,"🌱 Primeiros passos"),(25,"⭐ Aprendiz"),(50,"🔥 Dedicado"),(100,"🏆 Mestre")]:
        if total_ac >= qtd and nome_c not in p.get("conquistas", []):
            p.setdefault("conquistas", []).append(nome_c)
            novas.append(nome_c)
    salvar_perfil_ativo(p)
    return jsonify({"avancou": avancou, "novo_nivel": p[area]["nivel_atual"], "novas_conquistas": novas})

# ─────────────────────────────────────────────
# Rotas — IA generativa + Chatbot
# ─────────────────────────────────────────────

@app.route("/ia")
def ia_page():
    p = perfil_ativo()
    if not p: return redirect("/")
    return render_template("exercicio_ia.html", progresso=p,
                           ia_ok=ia_disponivel(), modelos=modelos_disponiveis())

@app.route("/chatbot")
def chatbot_page():
    p = perfil_ativo()
    if not p: return redirect("/")
    return render_template("chatbot.html", progresso=p, ia_ok=ia_disponivel())

@app.route("/api/ia/gerar", methods=["POST"])
def ia_gerar():
    p = perfil_ativo()
    if not p: return jsonify({"erro": "sem perfil"})
    if not IA_MODULO_OK:
        return jsonify({"erro": "Módulo de IA não instalado."})
    if not ia_disponivel():
        return jsonify({"erro": "Ollama não está rodando. Instale em ollama.com e execute: ollama run llama3.2"})
    data       = request.json
    tema       = data.get("tema", "").strip()
    nivel      = int(data.get("nivel", 1))
    quantidade = int(data.get("quantidade", 3))
    if not tema:
        return jsonify({"erro": "Digite um tema!"})
    resultado = gerar_licao_ia(tema, nivel, quantidade)
    if not resultado:
        return jsonify({"erro": "A IA não conseguiu gerar o exercício. Tente um tema diferente ou aguarde."})
    return jsonify(resultado)

@app.route("/api/ia/chat", methods=["POST"])
def ia_chat():
    p = perfil_ativo()
    if not p: return jsonify({"erro": "sem perfil"})
    if not IA_MODULO_OK:
        return jsonify({"erro": "Módulo de IA não instalado."})
    if not ia_disponivel():
        return jsonify({"erro": "Ollama não está rodando."})
    data      = request.json
    mensagem  = data.get("mensagem", "").strip()
    historico = data.get("historico", [])
    if not mensagem:
        return jsonify({"erro": "Mensagem vazia."})
    nivel_leit = p.get("leitura", {}).get("nivel_atual", 1)
    nivel_mat  = p.get("matematica", {}).get("nivel_atual", 1)
    contexto   = f"Nome: {p['nome']}. Nível de leitura: {nivel_leit}/5. Nível de matemática: {nivel_mat}/5."
    resposta   = chat_ia(mensagem, historico, contexto)
    if not resposta:
        return jsonify({"erro": "A IA não respondeu. Tente novamente."})
    return jsonify({"resposta": resposta})

@app.route("/api/ia/status")
def ia_status():
    return jsonify({
        "disponivel": ia_disponivel(),
        "modulo_ok":  IA_MODULO_OK,
        "modelos":    modelos_disponiveis(),
    })


# ─────────────────────────────────────────────
# Painel do Professor — Estilo Google Classroom
# ─────────────────────────────────────────────

SENHA_PROFESSOR = CONFIG["senha_professor"]

def professor_logado():
    return session.get("professor") == True

def _prof_redirect():
    return redirect("/professor")

# ── Login / Logout ──

@app.route("/professor/login", methods=["POST"])
def professor_login():
    if request.form.get("senha","") == SENHA_PROFESSOR:
        session["professor"] = True
        return redirect("/professor/turmas")
    return render_template("prof_login.html", erro="Senha incorreta.")

@app.route("/professor/logout")
def professor_logout():
    session.pop("professor", None)
    return redirect("/")

# ── Página principal — Turmas ──

@app.route("/professor")
@app.route("/professor/turmas")
def professor_turmas():
    if not professor_logado():
        return render_template("prof_login.html")
    perfis = carregar_perfis()
    turmas = carregar_turmas()
    avisos = carregar_avisos()
    atividades = carregar_atividades()
    # Enriquece turmas com stats
    turmas_lista = []
    for i, (nome, t) in enumerate(turmas.items()):
        s = stats_turma(t, perfis)
        avisos_turma = [a for a in avisos if a.get("turma") == nome]
        ativ_turma   = [a for a in atividades if a.get("turma") == nome]
        turmas_lista.append({
            **t,
            "stats": s,
            "cor": CORES_TURMA[i % len(CORES_TURMA)],
            "avisos_count": len(avisos_turma),
            "ativ_count": len(ativ_turma),
        })
    return render_template("prof_turmas.html",
                           turmas=turmas_lista, perfis=perfis,
                           total_alunos=len(perfis),
                           pagina="turmas")

# ── Detalhe de uma turma ──

@app.route("/professor/turma/<nome_turma>")
def professor_turma_detalhe(nome_turma):
    if not professor_logado(): return _prof_redirect()
    turmas = carregar_turmas()
    perfis = carregar_perfis()
    if nome_turma not in turmas: return redirect("/professor/turmas")
    turma = turmas[nome_turma]
    avisos = [a for a in carregar_avisos() if a.get("turma") == nome_turma]
    atividades = [a for a in carregar_atividades() if a.get("turma") == nome_turma]
    alunos_data = []
    for nome_aluno in turma.get("alunos", []):
        if nome_aluno in perfis:
            p = perfis[nome_aluno]
            alunos_data.append({
                "nome": nome_aluno,
                "avatar": p.get("avatar", "🌊"),
                "stats": calcular_stats_aluno(p),
                "perfil": p,
            })
    alunos_data.sort(key=lambda a: a["stats"]["aproveitamento"], reverse=True)
    i = list(turmas.keys()).index(nome_turma)
    return render_template("prof_turma_detalhe.html",
                           turma=turma, nome_turma=nome_turma,
                           cor=CORES_TURMA[i % len(CORES_TURMA)],
                           alunos=alunos_data, avisos=avisos,
                           atividades=atividades, modulos=MODULOS_INFO,
                           pagina="turmas")

# ── CRUD Turmas ──

@app.route("/professor/turmas/criar", methods=["POST"])
def criar_turma():
    if not professor_logado(): return _prof_redirect()
    nome  = request.form.get("nome","").strip()
    descricao = request.form.get("descricao","").strip()
    if not nome: return redirect("/professor/turmas")
    turmas = carregar_turmas()
    if nome not in turmas:
        turmas[nome] = {
            "nome": nome,
            "descricao": descricao,
            "codigo": gerar_codigo_turma(nome),
            "alunos": [],
            "criada_em": str(datetime.now()),
        }
        salvar_turmas(turmas)
    return redirect("/professor/turmas")

@app.route("/professor/turmas/excluir/<nome>", methods=["POST"])
def excluir_turma(nome):
    if not professor_logado(): return _prof_redirect()
    turmas = carregar_turmas()
    if nome in turmas:
        del turmas[nome]
        salvar_turmas(turmas)
    return redirect("/professor/turmas")

@app.route("/professor/turmas/adicionar_aluno", methods=["POST"])
def adicionar_aluno_turma():
    if not professor_logado(): return _prof_redirect()
    turma = request.form.get("turma","")
    aluno = request.form.get("aluno","")
    turmas = carregar_turmas()
    if turma in turmas and aluno and aluno not in turmas[turma]["alunos"]:
        turmas[turma]["alunos"].append(aluno)
        salvar_turmas(turmas)
    return redirect(f"/professor/turma/{turma}")

@app.route("/professor/turmas/remover_aluno", methods=["POST"])
def remover_aluno_turma():
    if not professor_logado(): return _prof_redirect()
    turma = request.form.get("turma","")
    aluno = request.form.get("aluno","")
    turmas = carregar_turmas()
    if turma in turmas and aluno in turmas[turma]["alunos"]:
        turmas[turma]["alunos"].remove(aluno)
        salvar_turmas(turmas)
    return redirect(f"/professor/turma/{turma}")

# ── Avisos ──

@app.route("/professor/avisos")
def professor_avisos():
    if not professor_logado(): return _prof_redirect()
    turmas = carregar_turmas()
    avisos = sorted(carregar_avisos(), key=lambda a: a.get("data",""), reverse=True)
    return render_template("prof_avisos.html",
                           avisos=avisos, turmas=turmas, pagina="avisos")

@app.route("/professor/avisos/criar", methods=["POST"])
def criar_aviso():
    if not professor_logado(): return _prof_redirect()
    titulo  = request.form.get("titulo","").strip()
    texto   = request.form.get("texto","").strip()
    turma   = request.form.get("turma","")
    if not titulo or not texto: return redirect("/professor/avisos")
    avisos = carregar_avisos()
    avisos.append({
        "id":     str(len(avisos)+1),
        "titulo": titulo,
        "texto":  texto,
        "turma":  turma,
        "data":   str(datetime.now()),
    })
    salvar_avisos(avisos)
    return redirect("/professor/avisos")

@app.route("/professor/avisos/excluir/<aviso_id>", methods=["POST"])
def excluir_aviso(aviso_id):
    if not professor_logado(): return _prof_redirect()
    avisos = [a for a in carregar_avisos() if a.get("id") != aviso_id]
    salvar_avisos(avisos)
    return redirect("/professor/avisos")

# ── Atividades ──

@app.route("/professor/atividades")
def professor_atividades():
    if not professor_logado(): return _prof_redirect()
    turmas = carregar_turmas()
    atividades = sorted(carregar_atividades(), key=lambda a: a.get("prazo",""), reverse=True)
    perfis = carregar_perfis()
    # Calcula conclusão de cada atividade
    for at in atividades:
        turma_nome = at.get("turma","")
        turma = carregar_turmas().get(turma_nome, {})
        alunos_turma = turma.get("alunos", [])
        modulo = at.get("modulo","")
        nivel_min = int(at.get("nivel_min", 1))
        concluidos = sum(
            1 for a in alunos_turma
            if a in perfis and perfis[a].get(modulo, {}).get("nivel_atual", 1) > nivel_min
        )
        at["concluidos"] = concluidos
        at["total_alunos"] = len(alunos_turma)
    return render_template("prof_atividades.html",
                           atividades=atividades, turmas=turmas,
                           modulos=MODULOS_INFO, pagina="atividades")

@app.route("/professor/atividades/criar", methods=["POST"])
def criar_atividade():
    if not professor_logado(): return _prof_redirect()
    titulo   = request.form.get("titulo","").strip()
    turma    = request.form.get("turma","")
    modulo   = request.form.get("modulo","")
    nivel_min = request.form.get("nivel_min","1")
    prazo    = request.form.get("prazo","")
    instrucoes = request.form.get("instrucoes","").strip()
    if not titulo or not turma or not modulo: return redirect("/professor/atividades")
    atividades = carregar_atividades()
    atividades.append({
        "id":        str(len(atividades)+1),
        "titulo":    titulo,
        "turma":     turma,
        "modulo":    modulo,
        "nivel_min": nivel_min,
        "prazo":     prazo,
        "instrucoes": instrucoes,
        "criada_em": str(datetime.now()),
    })
    salvar_atividades(atividades)
    return redirect("/professor/atividades")

@app.route("/professor/atividades/excluir/<at_id>", methods=["POST"])
def excluir_atividade(at_id):
    if not professor_logado(): return _prof_redirect()
    atividades = [a for a in carregar_atividades() if a.get("id") != at_id]
    salvar_atividades(atividades)
    return redirect("/professor/atividades")

# ── Alunos ──

@app.route("/professor/alunos")
def professor_alunos():
    if not professor_logado(): return _prof_redirect()
    perfis = carregar_perfis()
    turmas = carregar_turmas()
    filtro_turma = request.args.get("turma","")
    alunos = []
    for nome, p in perfis.items():
        turma_aluno = next((t for t, td in turmas.items() if nome in td.get("alunos",[])), "—")
        if filtro_turma and turma_aluno != filtro_turma: continue
        alunos.append({
            "nome": nome, "avatar": p.get("avatar","🌊"),
            "turma": turma_aluno,
            "stats": calcular_stats_aluno(p),
            "perfil": p,
        })
    alunos.sort(key=lambda a: a["stats"]["aproveitamento"], reverse=True)
    return render_template("prof_alunos.html",
                           alunos=alunos, turmas=turmas,
                           filtro_turma=filtro_turma,
                           modulos=MODULOS_INFO, pagina="alunos")

@app.route("/professor/aluno/<nome>")
def professor_aluno_detalhe(nome):
    if not professor_logado(): return _prof_redirect()
    perfis = carregar_perfis()
    turmas = carregar_turmas()
    if nome not in perfis: return redirect("/professor/alunos")
    p     = perfis[nome]
    stats = calcular_stats_aluno(p)
    turma = next((t for t, td in turmas.items() if nome in td.get("alunos",[])), None)
    return render_template("prof_aluno_detalhe.html",
                           aluno=p, stats=stats,
                           turma=turma, modulos=MODULOS_INFO, pagina="alunos")

# ── Relatórios ──

@app.route("/professor/relatorios")
def professor_relatorios():
    if not professor_logado(): return _prof_redirect()
    perfis  = carregar_perfis()
    turmas  = carregar_turmas()

    # ── Dados por módulo de ensino ──────────────────────────
    contagem_modulos = {"infantil": 0, "fundamental": 0, "medio": 0}
    for p in perfis.values():
        me = p.get("modulo_ensino", "fundamental")
        if me in contagem_modulos:
            contagem_modulos[me] += 1

    # ── Dados de desempenho por módulo clássico ─────────────
    dados_modulos = {}
    for chave, (nome_mod, icone, cor, _) in MODULOS_INFO.items():
        acertos = tentativas = 0
        for p in perfis.values():
            d = p.get(chave, {})
            acertos    += d.get("acertos_totais", 0)
            tentativas += d.get("tentativas_totais", 0)
        dados_modulos[chave] = {
            "nome": nome_mod, "cor": cor,
            "pct":      int(acertos/tentativas*100) if tentativas else 0,
            "acertos":  acertos,
            "tentativas": tentativas,
        }

    # ── Dados de desempenho por disciplina do Fundamental ───
    dados_fundamental = {}
    for chave, mat in MODULOS_FUNDAMENTAL.items():
        acertos = tentativas = 0
        for p in perfis.values():
            if p.get("modulo_ensino") != "fundamental": continue
            d = p.get(f"fund_{chave}", {})
            acertos    += d.get("acertos_totais", 0)
            tentativas += d.get("tentativas_totais", 0)
        dados_fundamental[chave] = {
            "nome": mat["titulo"], "cor": mat["cor"],
            "pct": int(acertos/tentativas*100) if tentativas else 0,
            "acertos": acertos, "tentativas": tentativas,
        }

    # ── Dados de desempenho por disciplina do Médio ─────────
    dados_medio = {}
    for chave, mat in MODULOS_MEDIO.items():
        acertos = tentativas = 0
        for p in perfis.values():
            if p.get("modulo_ensino") != "medio": continue
            d = p.get(f"medio_{chave}", {})
            acertos    += d.get("acertos_totais", 0)
            tentativas += d.get("tentativas_totais", 0)
        dados_medio[chave] = {
            "nome": mat["titulo"], "cor": mat["cor"],
            "pct": int(acertos/tentativas*100) if tentativas else 0,
            "acertos": acertos, "tentativas": tentativas,
        }

    # ── Dados por turma ──────────────────────────────────────
    dados_turmas = []
    for nome, t in turmas.items():
        s = stats_turma(t, perfis)
        dados_turmas.append({"nome": nome, **s})

    return render_template("prof_relatorios.html",
                           perfis=perfis, turmas=turmas,
                           dados_modulos=dados_modulos,
                           dados_fundamental=dados_fundamental,
                           dados_medio=dados_medio,
                           dados_turmas=dados_turmas,
                           contagem_modulos=contagem_modulos,
                           total_alunos=len(perfis),
                           pagina="relatorios")

# ── API avisos para o app do aluno ──

@app.route("/api/avisos")
def api_avisos():
    p = perfil_ativo()
    if not p: return jsonify([])
    turmas = carregar_turmas()
    nome = p["nome"]
    turma_aluno = next((t for t, td in turmas.items() if nome in td.get("alunos",[])), None)
    avisos = carregar_avisos()
    visiveis = [a for a in avisos if not a.get("turma") or a.get("turma") == turma_aluno]
    return jsonify(sorted(visiveis, key=lambda a: a.get("data",""), reverse=True)[:5])

@app.route("/api/professor/stats")
def professor_stats():
    if not professor_logado(): return jsonify({"erro": "não autorizado"}), 401
    perfis = carregar_perfis()
    return jsonify([{"nome": n, **calcular_stats_aluno(p)} for n, p in perfis.items()])
#
# ─────────────────────────────────────────────
# QR Code + inicialização com Waitress
# ─────────────────────────────────────────────

#def get_ip():
    #try:
        #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #s.connect(("8.8.8.8", 80))
        #ip = s.getsockname()[0]; s.close(); return ip
    #except Exception:
        #return "127.0.0.1"
#
#def gerar_qr_terminal(url):
    #try:
        #import qrcode
        #qr = qrcode.QRCode(border=1)
        #qr.add_data(url); qr.make(fit=True)
        #print("\n  📱 Escaneie o QR Code com o celular:\n")
        #qr.print_ascii(invert=True); print()
    #except ImportError:
        #print(f"\n  📱 Acesse no celular: {url}")
        #print("  (Para QR Code: pip install qrcode[pil])\n")
#
#if __name__ == "__main__":
    #ip  = get_ip()
    #url = f"http://{ip}:5000"
    #print("\n  🌊 EducaNorte — Servidor Web")
    #print("  ─────────────────────────────────────────")
    #print(f"  💻 No seu PC:   http://localhost:5000")
    #print(f"  📱 No celular:  {url}")
    #print(f"  👩‍🏫 Professor:   http://localhost:5000/professor")
    #print(f"  🤖 IA:          http://localhost:5000/ia")
    #print("  ─────────────────────────────────────────")
    #gerar_qr_terminal(url)
    #print("  Para parar: Ctrl+C\n")
    #srv  = CONFIG.get("servidor", {})
    #host    = srv.get("host", "0.0.0.0")
    #porta   = srv.get("porta", 5000)
    #threads = srv.get("threads", 8)
    #try:
        #from waitress import serve
        #print(f"  ✅ Servidor Waitress iniciado (robusto, multi-conexão)\n")
        #serve(app, host=host, port=porta, threads=threads)
    #except ImportError:
        #print("  ⚠️  Waitress não instalado. Rode: pip install waitress")
        #print("  Usando servidor Flask (menos estável)...\n")
        #app.run(host=host, port=porta, debug=False)