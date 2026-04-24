"""
Módulo de IA Offline — EducaNorte
Usa Ollama (llama3.2) rodando localmente.
Funcionalidades:
  1. Gerar exercícios de múltipla escolha por tema
  2. Chatbot educacional para o aluno conversar
"""

import json
import requests

OLLAMA_URL  = "http://localhost:11434"
MODEL       = "llama3.2"   # modelo padrão — pode trocar por llama3.2:1b para PCs mais fracos

# ─────────────────────────────────────────────
# Utilitários
# ─────────────────────────────────────────────

def ia_disponivel() -> bool:
    """Verifica se o Ollama está rodando e se o modelo está disponível."""
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=3)
        if r.status_code != 200:
            return False
        modelos = [m["name"] for m in r.json().get("models", [])]
        # Aceita variantes do modelo (llama3.2, llama3.2:latest, llama3.2:1b, etc.)
        return any(MODEL.split(":")[0] in m for m in modelos)
    except Exception:
        return False

def _chamar_ollama(prompt: str, timeout: int = 90) -> str | None:
    """Chama a API do Ollama e retorna o texto da resposta."""
    try:
        r = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=timeout
        )
        r.raise_for_status()
        return r.json().get("response", "").strip()
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return None
    except Exception:
        return None

def _extrair_json(texto: str) -> dict | None:
    """Extrai o primeiro bloco JSON válido de um texto."""
    if not texto:
        return None
    # Tenta achar o JSON entre { }
    inicio = texto.find("{")
    fim    = texto.rfind("}") + 1
    if inicio == -1 or fim == 0:
        return None
    try:
        return json.loads(texto[inicio:fim])
    except json.JSONDecodeError:
        return None


# ─────────────────────────────────────────────
# 1. Gerador de exercícios
# ─────────────────────────────────────────────

PROMPT_EXERCICIO = """Você é um professor de uma comunidade ribeirinha amazônica.
Gere {quantidade} perguntas de múltipla escolha em português sobre o tema: "{tema}".
Nível de dificuldade: {nivel} (1=muito fácil, 2=fácil, 3=médio, 4=difícil, 5=muito difícil).

Contextualize as perguntas para a realidade da Amazônia quando possível.

Responda SOMENTE com JSON válido, sem nenhum texto antes ou depois, no formato:
{{
  "titulo": "Título curto da lição",
  "texto": "Texto explicativo de 2 a 3 frases sobre o tema.",
  "perguntas": [
    {{
      "enunciado": "Texto da pergunta?",
      "opcoes": ["Opção A", "Opção B", "Opção C", "Opção D"],
      "resposta": "Opção correta exatamente como escrita acima",
      "dica": "Dica curta para o aluno"
    }}
  ]
}}"""


def gerar_licao_ia(tema: str, nivel: int = 1, quantidade: int = 3) -> dict | None:
    """
    Gera uma lição completa com perguntas de múltipla escolha.
    Retorna dict compatível com LICOES_LEITURA, LICOES_AMBIENTAL, etc.
    Retorna None se falhar.
    """
    prompt = PROMPT_EXERCICIO.format(
        tema=tema, nivel=nivel, quantidade=quantidade
    )
    texto = _chamar_ollama(prompt, timeout=90)
    if not texto:
        return None

    dados = _extrair_json(texto)
    if not dados:
        return None

    # Valida estrutura mínima
    if "perguntas" not in dados or "titulo" not in dados:
        return None

    # Garante que cada pergunta tem todos os campos
    perguntas_validas = []
    for p in dados["perguntas"]:
        if all(k in p for k in ["enunciado", "opcoes", "resposta", "dica"]):
            if isinstance(p["opcoes"], list) and len(p["opcoes"]) >= 2:
                perguntas_validas.append(p)

    if not perguntas_validas:
        return None

    dados["perguntas"] = perguntas_validas
    return dados


# ─────────────────────────────────────────────
# 2. Chatbot educacional
# ─────────────────────────────────────────────

SYSTEM_PROMPT = """Você é o Assistente Ribeirinho, um tutor educacional amigável para comunidades ribeirinhas da Amazônia.

Suas características:
- Fala em português brasileiro simples e claro
- Usa exemplos do cotidiano amazônico (rios, peixes, floresta, canoas)
- É paciente e encorajador, especialmente com crianças e adultos em alfabetização
- Responde perguntas sobre: leitura, matemática, meio ambiente, saúde e cultura ribeirinha
- Quando não sabe algo, admite honestamente
- Mantém respostas curtas e objetivas (máximo 4 parágrafos)
- Nunca usa linguagem técnica difícil sem explicar

Contexto atual do aluno: {contexto_aluno}

Histórico da conversa:
{historico}

Aluno: {mensagem}
Assistente Ribeirinho:"""


def chat_ia(mensagem: str, historico: list = None, contexto_aluno: str = "") -> str | None:
    """
    Envia uma mensagem para o chatbot e retorna a resposta.

    Args:
        mensagem: Mensagem atual do aluno
        historico: Lista de dicts [{"papel": "aluno"|"ia", "texto": "..."}]
        contexto_aluno: Info do perfil do aluno (nome, nível, etc.)

    Returns:
        Texto da resposta ou None se falhar
    """
    historico = historico or []

    # Formata o histórico
    hist_texto = ""
    for msg in historico[-6:]:  # últimas 6 mensagens para não estourar contexto
        papel = "Aluno" if msg.get("papel") == "aluno" else "Assistente Ribeirinho"
        hist_texto += f"{papel}: {msg['texto']}\n"

    prompt = SYSTEM_PROMPT.format(
        contexto_aluno=contexto_aluno or "Não informado",
        historico=hist_texto or "Nenhum histórico ainda.",
        mensagem=mensagem
    )

    resposta = _chamar_ollama(prompt, timeout=60)
    if not resposta:
        return None

    # Remove prefixos que o modelo às vezes adiciona
    for prefixo in ["Assistente Ribeirinho:", "Assistente:", "IA:"]:
        if resposta.startswith(prefixo):
            resposta = resposta[len(prefixo):].strip()

    return resposta


def modelos_disponiveis() -> list:
    """Retorna lista de modelos instalados no Ollama."""
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=3)
        if r.status_code == 200:
            return [m["name"] for m in r.json().get("models", [])]
    except Exception:
        pass
    return []
