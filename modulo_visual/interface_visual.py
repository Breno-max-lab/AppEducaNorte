"""
Módulo Visual — para pessoas que não sabem ler.
Interface com emojis grandes, botões touch, feedback por voz e cores.
Sem texto de instrução — guiado 100% por voz + imagens.
"""

import tkinter as tk
import sys
import os

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from modulo_visual.conteudo_visual import (
    ATIVIDADES_CONTAGEM,
    ATIVIDADES_IDENTIFICACAO,
    ATIVIDADES_COMPARACAO,
)

# Tenta importar voz
try:
    from modulo_voz.voz import ModuloVoz
    _voz = ModuloVoz()
except Exception:
    _voz = None


def falar(texto):
    try:
        if _voz and _voz.pode_falar:
            _voz.falar(texto)
    except Exception:
        pass


# ─────────────────────────────────────────────
# Paleta — mesma do projeto principal
# ─────────────────────────────────────────────

CORES = {
    "fundo":       "#0B2027",
    "painel":      "#13343B",
    "card":        "#1A4A52",
    "destaque":    "#40A68A",
    "destaque2":   "#F4A261",
    "acerto":      "#52B788",
    "erro":        "#E76F51",
    "texto":       "#E8F4F8",
    "texto_suave": "#8CBFCA",
    "borda":       "#2A6470",
    "hover":       "#2E7D8A",
    "amarelo":     "#FFD166",
}

FONTE_EMOJI   = ("Segoe UI Emoji", 52)
FONTE_EMOJI_G = ("Segoe UI Emoji", 72)
FONTE_NUM     = ("Segoe UI Emoji", 36)
FONTE_INSTR   = ("Georgia", 16, "bold")
FONTE_BTN     = ("Courier New", 13, "bold")
FONTE_PEQ     = ("Courier New", 11)


def _botao(pai, texto, cmd, cor=None, w=14, h=2):
    cor = cor or CORES["destaque"]
    b = tk.Button(pai, text=texto, command=cmd,
                  bg=cor, fg=CORES["fundo"], font=FONTE_BTN,
                  width=w, height=h, relief="flat", cursor="hand2",
                  activebackground=CORES["hover"], activeforeground=CORES["texto"])
    b.bind("<Enter>", lambda e: b.config(bg=CORES["hover"], fg=CORES["texto"]))
    b.bind("<Leave>", lambda e: b.config(bg=cor, fg=CORES["fundo"]))
    return b


# ─────────────────────────────────────────────
# Menu do módulo visual
# ─────────────────────────────────────────────

class TelaMenuVisual(tk.Frame):
    def __init__(self, master, ao_voltar):
        super().__init__(master, bg=CORES["painel"])
        self.ao_voltar = ao_voltar
        self._construir()
        falar("Bem-vindo! O que você quer aprender hoje?")

    def _construir(self):
        self.pack(fill="both", expand=True)

        # Cabeçalho
        cab = tk.Frame(self, bg=CORES["fundo"], height=60)
        cab.pack(fill="x")
        cab.pack_propagate(False)
        tk.Label(cab, text="🌊  Aprender com Figuras",
                 font=FONTE_INSTR, bg=CORES["fundo"],
                 fg=CORES["destaque"]).pack(side="left", padx=20, pady=12)

        tk.Label(self, text="O que você quer aprender?",
                 font=("Georgia", 20, "bold"),
                 bg=CORES["painel"], fg=CORES["texto"]).pack(pady=(30, 20))

        grade = tk.Frame(self, bg=CORES["painel"])
        grade.pack(pady=10)

        atividades = [
            ("🐟\n🐟🐟", "Contar", CORES["destaque"],  self._ir_contagem),
            ("🐬\n🦜🐊", "Conhecer\nAnimais",  CORES["destaque2"], self._ir_identificacao),
            ("⚖️\nQual tem\nmais?",  "Comparar", CORES["amarelo"],  self._ir_comparacao),
        ]

        for i, (icone, titulo, cor, cmd) in enumerate(atividades):
            card = tk.Frame(grade, bg=CORES["card"], width=190, height=210,
                            relief="flat", cursor="hand2")
            card.grid(row=0, column=i, padx=14, pady=8)
            card.grid_propagate(False)

            tk.Label(card, text=icone, font=FONTE_EMOJI,
                     bg=CORES["card"]).pack(pady=(18, 4))
            tk.Label(card, text=titulo, font=("Georgia", 14, "bold"),
                     bg=CORES["card"], fg=cor,
                     justify="center").pack()

            for w in [card] + card.winfo_children():
                w.bind("<Button-1>", lambda e, c=cmd: c())
            card.bind("<Enter>", lambda e, c=card: c.config(bg=CORES["hover"]))
            card.bind("<Leave>", lambda e, c=card: c.config(bg=CORES["card"]))

        _botao(self, "← Voltar", self.ao_voltar,
               cor=CORES["painel"], w=14).pack(pady=24)
        # reaplica cor do texto pra botão "fantasma"
        for w in self.winfo_children():
            if isinstance(w, tk.Button) and w.cget("text") == "← Voltar":
                w.config(fg=CORES["texto_suave"],
                         activeforeground=CORES["texto"])

    def _ir_contagem(self):
        falar("Vamos contar!")
        self._abrir(TelaContagem)

    def _ir_identificacao(self):
        falar("Vamos conhecer os animais!")
        self._abrir(TelaIdentificacao)

    def _ir_comparacao(self):
        falar("Vamos ver qual tem mais!")
        self._abrir(TelaComparacao)

    def _abrir(self, Classe):
        self.destroy()
        Classe(self.master, ao_voltar=lambda: self._reabrir())

    def _reabrir(self):
        TelaMenuVisual(self.master, self.ao_voltar)


# ─────────────────────────────────────────────
# Base comum para telas de atividade
# ─────────────────────────────────────────────

class TelaAtividadeBase(tk.Frame):
    """
    Gerencia o fluxo de perguntas de uma atividade.
    Subclasses implementam `_renderizar_pergunta()`.
    """

    def __init__(self, master, titulo, atividades, ao_voltar):
        super().__init__(master, bg=CORES["painel"])
        self.pack(fill="both", expand=True)
        self.ao_voltar = ao_voltar
        self.atividades = atividades
        self.nivel = 1
        self.indice = 0
        self.acertos = 0
        self.tentativas = 0

        # Cabeçalho fixo
        cab = tk.Frame(self, bg=CORES["fundo"], height=55)
        cab.pack(fill="x")
        cab.pack_propagate(False)
        tk.Label(cab, text=titulo, font=FONTE_INSTR,
                 bg=CORES["fundo"], fg=CORES["destaque"]).pack(side="left", padx=20, pady=10)
        self.lbl_pts = tk.Label(cab, text="✅ 0",
                                font=FONTE_PEQ, bg=CORES["fundo"],
                                fg=CORES["texto_suave"])
        self.lbl_pts.pack(side="right", padx=20)

        # Área central (substituída a cada pergunta)
        self.area = tk.Frame(self, bg=CORES["painel"])
        self.area.pack(fill="both", expand=True, padx=20, pady=10)

        self._carregar_atividade()

    def _carregar_atividade(self):
        ativ = self.atividades.get(self.nivel)
        if not ativ:
            self._fim()
            return
        self.perguntas = ativ["perguntas"]
        self.instrucao_voz = ativ["instrucao_voz"]
        falar(self.instrucao_voz)
        self._mostrar_pergunta()

    def _mostrar_pergunta(self):
        for w in self.area.winfo_children():
            w.destroy()

        if self.indice >= len(self.perguntas):
            self._proximo_nivel()
            return

        self.lbl_pts.config(text=f"✅ {self.acertos}")
        self.tentativas = 0
        self._renderizar_pergunta(self.perguntas[self.indice])

    def _renderizar_pergunta(self, pergunta):
        """Sobrescrever nas subclasses."""
        pass

    def _acertou(self, msg_voz):
        self.acertos += 1
        self.lbl_pts.config(text=f"✅ {self.acertos}")
        self._feedback(True, msg_voz)

    def _errou(self, msg_voz):
        self.tentativas += 1
        self._feedback(False, msg_voz)

    def _feedback(self, correto, msg_voz):
        falar(msg_voz)
        for w in self.area.winfo_children():
            w.destroy()

        cor = CORES["acerto"] if correto else CORES["erro"]
        emoji = "✅" if correto else "❌"

        tk.Label(self.area, text=emoji, font=("", 72),
                 bg=CORES["painel"]).pack(pady=(40, 10))
        tk.Label(self.area, text=msg_voz,
                 font=("Georgia", 16, "bold"),
                 bg=CORES["painel"], fg=cor,
                 wraplength=600, justify="center").pack()

        # Avança automaticamente após 1.8s
        self.after(1800, self._avancar)

    def _avancar(self):
        self.indice += 1
        self._mostrar_pergunta()

    def _proximo_nivel(self):
        nivel_max = max(self.atividades.keys())
        if self.nivel < nivel_max:
            self.nivel += 1
            self.indice = 0
            self._carregar_atividade()
        else:
            self._fim()

    def _fim(self):
        for w in self.area.winfo_children():
            w.destroy()

        total = sum(len(a["perguntas"]) for a in self.atividades.values())
        pct = self.acertos / total if total > 0 else 0
        emoji = "⭐⭐⭐" if pct >= 0.8 else ("⭐⭐" if pct >= 0.5 else "⭐")
        msg = "Muito bem!" if pct >= 0.8 else ("Bom trabalho!" if pct >= 0.5 else "Continue tentando!")

        falar(f"{msg} Você acertou {self.acertos} de {total}!")

        tk.Label(self.area, text=emoji, font=("", 54),
                 bg=CORES["painel"]).pack(pady=(30, 8))
        tk.Label(self.area, text=msg,
                 font=("Georgia", 22, "bold"),
                 bg=CORES["painel"], fg=CORES["acerto"]).pack()
        tk.Label(self.area,
                 text=f"{self.acertos} ✅  de  {total}",
                 font=("Georgia", 18),
                 bg=CORES["painel"], fg=CORES["texto"]).pack(pady=8)

        _botao(self.area, "← Voltar", self.ao_voltar, w=18).pack(pady=24)


# ─────────────────────────────────────────────
# Tela de Contagem
# ─────────────────────────────────────────────

class TelaContagem(TelaAtividadeBase):
    def __init__(self, master, ao_voltar):
        super().__init__(master, "🐟 Contar", ATIVIDADES_CONTAGEM, ao_voltar)

    def _renderizar_pergunta(self, p):
        falar(f"Quantos {p['visual'].replace('🐟','peixes').replace('🍌','bananas').replace('🍊','laranjas')} você vê?")

        # Exibe os emojis grandes
        tk.Label(self.area, text=p["visual"],
                 font=FONTE_EMOJI_G,
                 bg=CORES["painel"]).pack(pady=(20, 10))

        tk.Label(self.area, text="Quantos você vê? Toque no número:",
                 font=FONTE_INSTR, bg=CORES["painel"],
                 fg=CORES["texto_suave"]).pack(pady=(0, 16))

        # Botões com números grandes
        linha = tk.Frame(self.area, bg=CORES["painel"])
        linha.pack()

        for emoji_num, valor in zip(p["opcoes_visuais"], p["opcoes_valores"]):
            def ao_clicar(v=valor, perg=p):
                if v == perg["resposta"]:
                    self._acertou(perg["voz_acerto"])
                else:
                    self._errou(perg["voz_erro"])

            btn = tk.Button(
                linha, text=emoji_num,
                font=FONTE_NUM,
                command=ao_clicar,
                bg=CORES["card"], fg=CORES["texto"],
                width=3, height=2,
                relief="flat", cursor="hand2",
                activebackground=CORES["destaque"],
            )
            btn.pack(side="left", padx=12)


# ─────────────────────────────────────────────
# Tela de Identificação
# ─────────────────────────────────────────────

class TelaIdentificacao(TelaAtividadeBase):
    def __init__(self, master, ao_voltar):
        super().__init__(master, "🐬 Conhecer", ATIVIDADES_IDENTIFICACAO, ao_voltar)

    def _renderizar_pergunta(self, p):
        falar(p["pergunta_voz"])

        tk.Label(self.area, text=p["pergunta_visual"],
                 font=FONTE_INSTR, bg=CORES["painel"],
                 fg=CORES["texto"], wraplength=600,
                 justify="center").pack(pady=(16, 20))

        linha = tk.Frame(self.area, bg=CORES["painel"])
        linha.pack()

        for opcao in p["opcoes"]:
            def ao_clicar(op=opcao, perg=p):
                if op["correto"]:
                    self._acertou(perg["voz_acerto"])
                else:
                    self._errou(perg["voz_erro"])

            card = tk.Frame(linha, bg=CORES["card"],
                            width=170, height=170,
                            relief="flat", cursor="hand2")
            card.pack(side="left", padx=14)
            card.pack_propagate(False)

            tk.Label(card, text=opcao["emoji"],
                     font=FONTE_EMOJI_G,
                     bg=CORES["card"]).pack(pady=(18, 4))

            for w in [card] + card.winfo_children():
                w.bind("<Button-1>", lambda e, c=ao_clicar: c())
            card.bind("<Enter>", lambda e, c=card: c.config(bg=CORES["hover"]))
            card.bind("<Leave>", lambda e, c=card: c.config(bg=CORES["card"]))


# ─────────────────────────────────────────────
# Tela de Comparação
# ─────────────────────────────────────────────

class TelaComparacao(TelaAtividadeBase):
    def __init__(self, master, ao_voltar):
        super().__init__(master, "⚖️ Comparar", ATIVIDADES_COMPARACAO, ao_voltar)

    def _renderizar_pergunta(self, p):
        falar(p["pergunta_voz"])

        tk.Label(self.area, text="Toque no grupo que tem MAIS:",
                 font=FONTE_INSTR, bg=CORES["painel"],
                 fg=CORES["texto_suave"]).pack(pady=(16, 20))

        linha = tk.Frame(self.area, bg=CORES["painel"])
        linha.pack()

        for opcao in p["opcoes"]:
            def ao_clicar(op=opcao, perg=p):
                if op["correto"]:
                    self._acertou(perg["voz_acerto"])
                else:
                    self._errou(perg["voz_erro"])

            card = tk.Frame(linha, bg=CORES["card"],
                            width=240, height=180,
                            relief="flat", cursor="hand2")
            card.pack(side="left", padx=20)
            card.pack_propagate(False)

            tk.Label(card, text=opcao["visual"],
                     font=("Segoe UI Emoji", 32),
                     bg=CORES["card"],
                     wraplength=220,
                     justify="center").pack(expand=True)

            for w in [card] + card.winfo_children():
                w.bind("<Button-1>", lambda e, c=ao_clicar: c())
            card.bind("<Enter>", lambda e, c=card: c.config(bg=CORES["hover"]))
            card.bind("<Leave>", lambda e, c=card: c.config(bg=CORES["card"]))


# ─────────────────────────────────────────────
# Ponto de entrada standalone (teste isolado)
# ─────────────────────────────────────────────

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Módulo Visual — Assistente Ribeirinho")
    root.geometry("800x480")
    root.configure(bg=CORES["painel"])
    TelaMenuVisual(root, ao_voltar=root.destroy)
    root.mainloop()
