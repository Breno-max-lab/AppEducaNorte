"""
Interface Gráfica — Assistente Ribeirinho (Design Moderno)
Visual renovado: azul noturno profundo, cards com acento colorido,
barra de navegação, progresso visual por módulo.
100% offline, compatível com Raspberry Pi + tela touch.
"""

import tkinter as tk
from tkinter import messagebox
import os
import sys
from datetime import datetime

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from modulo_alfabetizacao.conteudo import LICOES_LEITURA, LICOES_MATEMATICA
from modulo_alfabetizacao.main import carregar_progresso, salvar_progresso

try:
    from modulo_voz.voz import ModuloVoz
    VOZ_DISPONIVEL = True
except ImportError:
    VOZ_DISPONIVEL = False

try:
    from modulo_visual.interface_visual import TelaMenuVisual
    VISUAL_DISPONIVEL = True
except ImportError:
    VISUAL_DISPONIVEL = False


# ─────────────────────────────────────────────
# Design System
# ─────────────────────────────────────────────

C = {
    "bg":          "#0D1B2A",
    "topbar":      "#0A1520",
    "card":        "#112233",
    "card_hover":  "#142840",
    "borda":       "#1E3A4A",
    "teal":        "#00C9A7",
    "teal_bg":     "#0E2A2A",
    "laranja":     "#F4A261",
    "laranja_bg":  "#2A1A0A",
    "amarelo":     "#FFD166",
    "amarelo_bg":  "#2A2208",
    "roxo":        "#9B72CF",
    "roxo_bg":     "#1A0D2A",
    "verde":       "#4ADE80",
    "verde_bg":    "#0E2D1E",
    "erro":        "#E76F51",
    "erro_bg":     "#2A100A",
    "texto":       "#D0ECF4",
    "texto2":      "#7ABFCC",
    "texto3":      "#3A6A78",
    "branco":      "#E8F4F8",
}

F = {
    "titulo":    ("Segoe UI", 20, "bold"),
    "subtitulo": ("Segoe UI", 14, "bold"),
    "corpo":     ("Segoe UI", 13),
    "botao":     ("Segoe UI", 13, "bold"),
    "pequeno":   ("Segoe UI", 11),
    "mini":      ("Segoe UI", 10),
    "grande":    ("Segoe UI", 26, "bold"),
    "card_tit":  ("Segoe UI", 13, "bold"),
}


# ─────────────────────────────────────────────
# Componentes base
# ─────────────────────────────────────────────

def _lbl(pai, texto, fonte=None, cor=None, bg=None, **kw):
    return tk.Label(pai, text=texto, font=fonte or F["corpo"],
                    fg=cor or C["texto"], bg=bg or C["bg"], **kw)


def _btn(pai, texto, cmd, bg=None, fg=None, fonte=None, w=18, h=2):
    bg = bg or C["teal"]
    fg = fg or C["bg"]
    btn = tk.Button(pai, text=texto, command=cmd,
                    bg=bg, fg=fg, font=fonte or F["botao"],
                    width=w, height=h, relief="flat", cursor="hand2",
                    activebackground=C["card_hover"],
                    activeforeground=C["texto"], bd=0)
    btn.bind("<Enter>", lambda e: btn.config(bg=C["teal"], fg=C["bg"]))
    btn.bind("<Leave>", lambda e: btn.config(bg=bg, fg=fg))
    return btn


def _sep(pai):
    tk.Frame(pai, bg=C["borda"], height=1).pack(fill="x")


# ─────────────────────────────────────────────
# Topbar
# ─────────────────────────────────────────────

class Topbar(tk.Frame):
    def __init__(self, master, nome, nivel_leit=1, nivel_mat=1):
        super().__init__(master, bg=C["topbar"], height=52)
        self.pack(fill="x")
        self.pack_propagate(False)
        self._construir(nome, nivel_leit, nivel_mat)
        _sep(master)

    def _construir(self, nome, nl, nm):
        esq = tk.Frame(self, bg=C["topbar"])
        esq.pack(side="left", padx=18, pady=8)

        icone = tk.Frame(esq, bg=C["teal"], width=30, height=30)
        icone.pack(side="left")
        icone.pack_propagate(False)
        tk.Label(icone, text="🌊", font=("Segoe UI Emoji", 14),
                 bg=C["teal"]).pack(expand=True)

        tk.Label(esq, text="  Assistente Ribeirinho",
                 font=("Segoe UI", 13, "bold"),
                 fg=C["branco"], bg=C["topbar"]).pack(side="left")

        dir_ = tk.Frame(self, bg=C["topbar"])
        dir_.pack(side="right", padx=18)

        badge = tk.Frame(dir_, bg="#1A2E3E")
        badge.pack(side="right", ipady=5, ipadx=10)

        av = tk.Frame(badge, bg=C["teal"], width=22, height=22)
        av.pack(side="left", padx=(0, 6))
        av.pack_propagate(False)
        tk.Label(av, text=(nome[0].upper() if nome else "?"),
                 font=("Segoe UI", 10, "bold"),
                 fg=C["bg"], bg=C["teal"]).pack(expand=True)

        tk.Label(badge, text=nome, font=F["mini"],
                 fg=C["texto2"], bg="#1A2E3E").pack(side="left")

        pill = tk.Frame(badge, bg=C["verde_bg"])
        pill.pack(side="left", padx=(8, 0))
        tk.Label(pill, text=f"Nv.{max(nl, nm)}",
                 font=("Segoe UI", 9, "bold"),
                 fg=C["verde"], bg=C["verde_bg"],
                 padx=6, pady=1).pack()


# ─────────────────────────────────────────────
# Navbar
# ─────────────────────────────────────────────

class Navbar(tk.Frame):
    def __init__(self, master, ativo="inicio", callbacks=None):
        super().__init__(master, bg=C["topbar"], height=42)
        self.pack(side="bottom", fill="x")
        self.pack_propagate(False)
        _sep(master)
        callbacks = callbacks or {}
        itens = [
            ("inicio",     "⌂  Início"),
            ("atividades", "◈  Atividades"),
            ("progresso",  "◉  Progresso"),
        ]
        for chave, rotulo in itens:
            eh = chave == ativo
            tk.Button(self, text=rotulo,
                      command=callbacks.get(chave, lambda: None),
                      bg=C["teal_bg"] if eh else C["topbar"],
                      fg=C["teal"] if eh else C["texto3"],
                      font=("Segoe UI", 11, "bold") if eh else F["pequeno"],
                      relief="flat", cursor="hand2", padx=20,
                      activebackground=C["teal_bg"],
                      activeforeground=C["teal"], bd=0).pack(side="left", fill="y")


# ─────────────────────────────────────────────
# Card de módulo
# ─────────────────────────────────────────────

class CardModulo(tk.Frame):
    def __init__(self, master, icone, titulo, descricao,
                 cor, cor_bg_ic, nivel, total_niveis, cmd):
        super().__init__(master, bg=C["card"], bd=0,
                         cursor="hand2", width=178, height=195)
        self.pack_propagate(False)
        self.cmd = cmd
        self.cor = cor
        self._construir(icone, titulo, descricao, cor, cor_bg_ic, nivel, total_niveis)
        self._configurar_eventos()

    def _construir(self, icone, titulo, desc, cor, cor_bg_ic, nivel, total):
        tk.Frame(self, bg=cor, height=4).pack(fill="x")

        corpo = tk.Frame(self, bg=C["card"], padx=14)
        corpo.pack(fill="both", expand=True, pady=(10, 12))

        ic = tk.Frame(corpo, bg=cor_bg_ic, width=38, height=38)
        ic.pack(anchor="w")
        ic.pack_propagate(False)
        tk.Label(ic, text=icone, font=("Segoe UI Emoji", 18),
                 bg=cor_bg_ic).pack(expand=True)

        tk.Label(corpo, text=titulo, font=F["card_tit"],
                 fg=C["branco"], bg=C["card"],
                 anchor="w").pack(fill="x", pady=(8, 0))

        tk.Label(corpo, text=desc, font=F["mini"],
                 fg=C["texto3"], bg=C["card"],
                 anchor="w", justify="left",
                 wraplength=150).pack(fill="x", pady=(2, 8))

        pct = min((nivel - 1) / max(total, 1), 1.0)
        bwrap = tk.Frame(corpo, bg="#1A2E3E", height=3)
        bwrap.pack(fill="x")
        if pct > 0:
            tk.Frame(bwrap, bg=cor, height=3).place(relwidth=pct, relheight=1)

        badge = tk.Frame(corpo, bg=cor_bg_ic)
        badge.pack(anchor="w", pady=(6, 0))
        tk.Label(badge, text=f"Nível {nivel}",
                 font=("Segoe UI", 9, "bold"),
                 fg=cor, bg=cor_bg_ic, padx=6, pady=2).pack()

    def _configurar_eventos(self):
        def _rec(widget):
            widget.bind("<Button-1>", lambda e: self.cmd())
            widget.bind("<Enter>",    lambda e: self._hover(True))
            widget.bind("<Leave>",    lambda e: self._hover(False))
            for child in widget.winfo_children():
                _rec(child)
        _rec(self)

    def _hover(self, entrou):
        cor = C["card_hover"] if entrou else C["card"]
        def _rec(w):
            try:
                if w.cget("bg") in (C["card"], C["card_hover"]):
                    w.config(bg=cor)
            except Exception:
                pass
            for c in w.winfo_children():
                _rec(c)
        _rec(self)


# ─────────────────────────────────────────────
# Tela de boas-vindas
# ─────────────────────────────────────────────

class TelaBemVindo(tk.Frame):
    def __init__(self, master, ao_entrar):
        super().__init__(master, bg=C["bg"])
        self.ao_entrar = ao_entrar
        self.pack(fill="both", expand=True)
        self._construir()

    def _construir(self):
        centro = tk.Frame(self, bg=C["bg"])
        centro.place(relx=0.5, rely=0.5, anchor="center")

        logo = tk.Frame(centro, bg=C["teal"], width=64, height=64)
        logo.pack()
        logo.pack_propagate(False)
        tk.Label(logo, text="🌊", font=("Segoe UI Emoji", 32),
                 bg=C["teal"]).pack(expand=True)

        tk.Label(centro, text="Assistente Ribeirinho",
                 font=("Segoe UI", 22, "bold"),
                 fg=C["teal"], bg=C["bg"]).pack(pady=(16, 4))
        tk.Label(centro, text="Aprender é navegar em novos rios.",
                 font=F["corpo"], fg=C["texto3"], bg=C["bg"]).pack(pady=(0, 32))

        card = tk.Frame(centro, bg=C["card"])
        card.pack(ipadx=32, ipady=24)

        tk.Label(card, text="Qual é o seu nome?",
                 font=F["subtitulo"], fg=C["texto"], bg=C["card"]).pack(pady=(0, 10))

        self.entrada = tk.Entry(card, font=("Segoe UI", 14),
                                bg="#1A2E3E", fg=C["branco"],
                                insertbackground=C["teal"],
                                relief="flat", width=22, justify="center", bd=0)
        self.entrada.pack(ipady=10, pady=(0, 16))
        self.entrada.focus()
        self.entrada.bind("<Return>", lambda e: self._entrar())
        _btn(card, "Entrar  →", self._entrar, w=24, h=2).pack()

    def _entrar(self):
        self.ao_entrar(self.entrada.get().strip() or "Estudante")


# ─────────────────────────────────────────────
# Menu principal
# ─────────────────────────────────────────────

class TelaMenuPrincipal(tk.Frame):
    def __init__(self, master, progresso, callbacks):
        super().__init__(master, bg=C["bg"])
        self.progresso = progresso
        self.callbacks = callbacks
        self.pack(fill="both", expand=True)
        self._construir()

    def _construir(self):
        p = self.progresso
        nl = p["leitura"]["nivel_atual"]
        nm = p["matematica"]["nivel_atual"]
        Topbar(self, p["nome"], nl, nm)

        hora = datetime.now().hour
        saudacao = "Bom dia" if hora < 12 else ("Boa tarde" if hora < 18 else "Boa noite")

        meio = tk.Frame(self, bg=C["bg"])
        meio.pack(fill="both", expand=True, padx=28, pady=(18, 0))

        tk.Label(meio, text=f"{saudacao}, {p['nome']}!",
                 font=("Segoe UI", 18, "bold"),
                 fg=C["branco"], bg=C["bg"]).pack(anchor="w")
        tk.Label(meio, text="O que vamos explorar hoje?",
                 font=F["pequeno"], fg=C["texto3"], bg=C["bg"]).pack(anchor="w", pady=(2, 16))

        grade = tk.Frame(meio, bg=C["bg"])
        grade.pack(anchor="w")

        modulos = [
            ("📖", "Leitura",      "Vogais, sílabas\ne compreensão",
             C["teal"],    C["teal_bg"],    nl, 3, self.callbacks["leitura"]),
            ("🔢", "Matemática",    "Contagem, números\ne problemas",
             C["laranja"], C["laranja_bg"], nm, 3, self.callbacks["matematica"]),
            ("🖼️", "Com Figuras",  "Para quem ainda\nnão lê",
             C["amarelo"], C["amarelo_bg"], 1,  2, self.callbacks["visual"]),
            ("📊", "Meu Progresso","Seus acertos\ne conquistas",
             C["roxo"],    C["roxo_bg"],    1,  1, self.callbacks["progresso"]),
        ]

        for i, args in enumerate(modulos):
            CardModulo(grade, *args).grid(row=0, column=i, padx=10, pady=4)

        Navbar(self, ativo="inicio", callbacks={
            "inicio":     self.callbacks.get("menu",      lambda: None),
            "atividades": self.callbacks.get("leitura",   lambda: None),
            "progresso":  self.callbacks.get("progresso", lambda: None),
        })


# ─────────────────────────────────────────────
# Tela de lição
# ─────────────────────────────────────────────

class TelaLicao(tk.Frame):
    def __init__(self, master, area, licoes, progresso, ao_terminar):
        super().__init__(master, bg=C["bg"])
        self.area = area
        self.licoes = licoes
        self.progresso = progresso
        self.ao_terminar = ao_terminar
        self.chave = "leitura" if area == "Leitura" else "matematica"
        self.nivel = progresso[self.chave]["nivel_atual"]
        self.perguntas = []
        self.indice = 0
        self.acertos = 0
        self.tentativas_pergunta = 0
        self.resposta_selecionada = tk.StringVar()
        self.pack(fill="both", expand=True)
        self._construir()
        self._carregar_licao()

    def _construir(self):
        top = tk.Frame(self, bg=C["topbar"], height=52)
        top.pack(fill="x")
        top.pack_propagate(False)
        _sep(self)

        esq = tk.Frame(top, bg=C["topbar"])
        esq.pack(side="left", padx=16, pady=10)
        _btn(esq, "←", self.ao_terminar, bg=C["card"],
             fg=C["texto2"], w=3, h=1, fonte=F["subtitulo"]).pack(side="left")
        self.lbl_titulo = tk.Label(esq, text="", font=F["subtitulo"],
                                   fg=C["teal"], bg=C["topbar"])
        self.lbl_titulo.pack(side="left", padx=12)

        self.lbl_pts = tk.Label(top, text="✓ 0", font=F["pequeno"],
                                fg=C["verde"], bg=C["topbar"])
        self.lbl_pts.pack(side="right", padx=20)

        self.barra_wrap = tk.Frame(self, bg="#1A2E3E", height=4)
        self.barra_wrap.pack(fill="x")
        self.barra_fill = tk.Frame(self.barra_wrap, bg=C["teal"], height=4)
        self.barra_fill.place(relwidth=0, relheight=1)

        self.frame_texto = tk.Frame(self, bg=C["card"], padx=20, pady=14)
        self.frame_texto.pack(fill="x", padx=24, pady=(18, 0))
        self.lbl_texto = tk.Label(self.frame_texto, text="",
                                  font=("Segoe UI", 13, "italic"),
                                  fg=C["texto2"], bg=C["card"],
                                  wraplength=680, justify="left")
        self.lbl_texto.pack(anchor="w")

        self.lbl_pergunta = tk.Label(self, text="",
                                     font=("Segoe UI", 15, "bold"),
                                     fg=C["branco"], bg=C["bg"],
                                     wraplength=680, justify="center")
        self.lbl_pergunta.pack(pady=(16, 10), padx=24)

        self.frame_opcoes = tk.Frame(self, bg=C["bg"])
        self.frame_opcoes.pack()
        self.botoes_opcao = []
        for _ in range(4):
            btn = tk.Radiobutton(
                self.frame_opcoes, text="",
                variable=self.resposta_selecionada, value="",
                bg=C["card"], fg=C["texto"],
                selectcolor=C["teal"], activebackground=C["card_hover"],
                font=F["corpo"], relief="flat", indicatoron=False,
                width=38, height=2, cursor="hand2", bd=0,
                highlightthickness=0)
            btn.pack(pady=3, ipady=4)
            self.botoes_opcao.append(btn)

        self.lbl_feedback = tk.Label(self, text="", font=F["subtitulo"],
                                     fg=C["verde"], bg=C["bg"])
        self.lbl_feedback.pack(pady=(8, 0))
        self.lbl_dica = tk.Label(self, text="", font=F["pequeno"],
                                 fg=C["laranja"], bg=C["bg"],
                                 wraplength=680, justify="center")
        self.lbl_dica.pack()

        self.btn_confirmar = _btn(self, "Confirmar resposta",
                                  self._confirmar, w=28, h=2)
        self.btn_confirmar.pack(pady=12)

    def _carregar_licao(self):
        licao = self.licoes.get(self.nivel)
        if not licao:
            return
        self.perguntas = licao["perguntas"]
        self.lbl_titulo.config(
            text=f"{self.area}  ·  Nível {self.nivel}: {licao['titulo']}")
        texto = licao.get("texto") or licao.get("contexto", "")
        if texto:
            self.lbl_texto.config(text=f"📖  {texto}")
        else:
            self.frame_texto.pack_forget()
        self._mostrar_pergunta()

    def _mostrar_pergunta(self):
        if self.indice >= len(self.perguntas):
            self._resultado_final()
            return
        self.tentativas_pergunta = 0
        p = self.perguntas[self.indice]
        total = len(self.perguntas)
        self.barra_fill.place(relwidth=self.indice / total, relheight=1)
        self.lbl_pts.config(text=f"✓ {self.acertos}")
        self.lbl_pergunta.config(text=f"❓  {p['enunciado']}")
        self.lbl_feedback.config(text="")
        self.lbl_dica.config(text="")
        self.resposta_selecionada.set("")
        for i, btn in enumerate(self.botoes_opcao):
            if i < len(p["opcoes"]):
                btn.config(text=f"  {p['opcoes'][i]}", value=p["opcoes"][i],
                           state="normal", bg=C["card"], fg=C["texto"])
                btn.pack()
            else:
                btn.pack_forget()
        self.btn_confirmar.config(state="normal",
                                  text="Confirmar resposta",
                                  command=self._confirmar)

    def _confirmar(self):
        p = self.perguntas[self.indice]
        resp = self.resposta_selecionada.get()
        if not resp:
            self.lbl_feedback.config(text="⚠  Selecione uma opção!", fg=C["laranja"])
            return
        self.tentativas_pergunta += 1
        if resp.lower() == p["resposta"].lower():
            self.acertos += 1
            self.lbl_feedback.config(text="✓  Correto! Muito bem!", fg=C["verde"])
            self.lbl_dica.config(text="")
            for btn in self.botoes_opcao:
                if btn.cget("value") == resp:
                    btn.config(bg=C["teal_bg"], fg=C["teal"])
            self.btn_confirmar.config(text="Próxima  →", command=self._proxima)
        else:
            self.lbl_feedback.config(text="✗  Não foi dessa vez!", fg=C["erro"])
            for btn in self.botoes_opcao:
                if btn.cget("value") == resp:
                    btn.config(bg=C["erro_bg"], fg=C["erro"])
            if self.tentativas_pergunta == 1:
                self.lbl_dica.config(text=f"💡  {p['dica']}")
            else:
                self.lbl_dica.config(text=f"Resposta correta: {p['resposta']}")
                self.btn_confirmar.config(text="Próxima  →", command=self._proxima)

    def _proxima(self):
        self.indice += 1
        for btn in self.botoes_opcao:
            btn.config(bg=C["card"], fg=C["texto"])
        self._mostrar_pergunta()

    def _resultado_final(self):
        self.barra_fill.place(relwidth=1, relheight=1)
        for w in self.winfo_children():
            if w is not self.barra_wrap:
                try: w.pack_forget()
                except: pass

        total = len(self.perguntas)
        pct = self.acertos / total
        if pct >= 0.8:   emoji, msg, cor = "⭐⭐⭐", "Excelente trabalho!", C["teal"]
        elif pct >= 0.5: emoji, msg, cor = "⭐⭐",  "Bom trabalho!",       C["laranja"]
        else:            emoji, msg, cor = "⭐",    "Continue tentando!",  C["texto3"]

        res = tk.Frame(self, bg=C["bg"])
        res.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(res, text=emoji, font=("Segoe UI Emoji", 44),
                 bg=C["bg"]).pack(pady=(0, 8))
        tk.Label(res, text=msg, font=("Segoe UI", 20, "bold"),
                 fg=cor, bg=C["bg"]).pack()
        tk.Label(res, text=f"{self.acertos} de {total} corretas",
                 font=F["subtitulo"], fg=C["texto2"], bg=C["bg"]).pack(pady=6)

        nivel_max = max(self.licoes.keys())
        if pct >= 0.7 and self.nivel < nivel_max:
            prox = self.nivel + 1
            self.progresso[self.chave]["nivel_atual"] = prox
            tk.Label(res, text=f"🎉  Você avançou para o Nível {prox}!",
                     font=F["subtitulo"], fg=C["amarelo"], bg=C["bg"]).pack(pady=4)

        self.progresso[self.chave]["acertos_totais"] += self.acertos
        self.progresso[self.chave]["tentativas_totais"] += total
        salvar_progresso(self.progresso)
        _btn(res, "← Voltar ao menu", self.ao_terminar, w=22, h=2).pack(pady=20)


# ─────────────────────────────────────────────
# Tela de progresso
# ─────────────────────────────────────────────

class TelaProgresso(tk.Frame):
    def __init__(self, master, progresso, ao_voltar):
        super().__init__(master, bg=C["bg"])
        self.progresso = progresso
        self.ao_voltar = ao_voltar
        self.pack(fill="both", expand=True)
        self._construir()

    def _construir(self):
        p = self.progresso
        Topbar(self, p["nome"],
               p["leitura"]["nivel_atual"],
               p["matematica"]["nivel_atual"])

        meio = tk.Frame(self, bg=C["bg"])
        meio.pack(fill="both", expand=True, padx=28, pady=18)

        tk.Label(meio, text="Meu Progresso",
                 font=("Segoe UI", 18, "bold"),
                 fg=C["branco"], bg=C["bg"]).pack(anchor="w")
        tk.Label(meio, text=f"Olá, {p['nome']}! Veja o que você conquistou.",
                 font=F["pequeno"], fg=C["texto3"], bg=C["bg"]).pack(anchor="w", pady=(2, 16))

        for area, chave, icone, cor, cor_bg in [
            ("Leitura",    "leitura",    "📖", C["teal"],    C["teal_bg"]),
            ("Matemática", "matematica", "🔢", C["laranja"], C["laranja_bg"]),
        ]:
            d = p[chave]
            pct = d["acertos_totais"] / d["tentativas_totais"] if d["tentativas_totais"] > 0 else 0

            card = tk.Frame(meio, bg=C["card"])
            card.pack(fill="x", pady=6)
            tk.Frame(card, bg=cor, width=4).pack(side="left", fill="y")

            corpo = tk.Frame(card, bg=C["card"], padx=16, pady=12)
            corpo.pack(fill="x", side="left", expand=True)

            linha = tk.Frame(corpo, bg=C["card"])
            linha.pack(fill="x")
            tk.Label(linha, text=f"{icone}  {area}",
                     font=F["subtitulo"], fg=C["branco"],
                     bg=C["card"]).pack(side="left")

            badge = tk.Frame(linha, bg=cor_bg)
            badge.pack(side="right")
            tk.Label(badge, text=f"Nível {d['nivel_atual']}",
                     font=("Segoe UI", 10, "bold"),
                     fg=cor, bg=cor_bg, padx=8, pady=2).pack()

            bwrap = tk.Frame(corpo, bg="#1A2E3E", height=6)
            bwrap.pack(fill="x", pady=(10, 4))
            if pct > 0:
                tk.Frame(bwrap, bg=cor, height=6).place(relwidth=pct, relheight=1)

            tk.Label(corpo,
                     text=f"{d['acertos_totais']} acertos de {d['tentativas_totais']} perguntas  ({int(pct*100)}%)",
                     font=F["mini"], fg=C["texto3"], bg=C["card"]).pack(anchor="w")

        _btn(meio, "← Voltar ao menu", self.ao_voltar, w=22, h=2).pack(pady=20, anchor="w")

        Navbar(self, ativo="progresso", callbacks={
            "inicio":    self.ao_voltar,
            "progresso": lambda: None,
        })


# ─────────────────────────────────────────────
# Aplicação principal
# ─────────────────────────────────────────────

class AssistenteRibeirinho:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Assistente Ribeirinho")
        self.root.configure(bg=C["bg"])
        self.root.geometry("800x480")
        self.root.resizable(True, True)
        self.progresso = carregar_progresso()
        self.tela_atual = None
        self.voz = ModuloVoz() if VOZ_DISPONIVEL else None
        self._mostrar_tela_inicial()

    def _limpar(self):
        if self.tela_atual:
            self.tela_atual.destroy()

    def _mostrar_tela_inicial(self):
        self._limpar()
        if self.progresso["nome"]:
            self._mostrar_menu()
        else:
            self.tela_atual = TelaBemVindo(self.root, self._cadastrar_nome)

    def _cadastrar_nome(self, nome):
        self.progresso["nome"] = nome
        salvar_progresso(self.progresso)
        self._mostrar_menu()

    def _mostrar_menu(self):
        self._limpar()
        self.tela_atual = TelaMenuPrincipal(
            self.root, self.progresso,
            callbacks={
                "menu":       self._mostrar_menu,
                "leitura":    self._iniciar_leitura,
                "matematica": self._iniciar_matematica,
                "visual":     self._iniciar_visual,
                "progresso":  self._mostrar_progresso,
            }
        )

    def _iniciar_leitura(self):
        self._limpar()
        self.tela_atual = TelaLicao(
            self.root, "Leitura", LICOES_LEITURA,
            self.progresso, self._mostrar_menu)

    def _iniciar_matematica(self):
        self._limpar()
        self.tela_atual = TelaLicao(
            self.root, "Matemática", LICOES_MATEMATICA,
            self.progresso, self._mostrar_menu)

    def _iniciar_visual(self):
        self._limpar()
        if VISUAL_DISPONIVEL:
            self.tela_atual = TelaMenuVisual(self.root, ao_voltar=self._mostrar_menu)
        else:
            messagebox.showinfo("Indisponível", "Módulo visual não encontrado.")
            self._mostrar_menu()

    def _mostrar_progresso(self):
        self._limpar()
        self.tela_atual = TelaProgresso(
            self.root, self.progresso, self._mostrar_menu)

    def rodar(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = AssistenteRibeirinho()
    app.rodar()
