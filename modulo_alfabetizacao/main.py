"""
Motor principal do Módulo de Alfabetização e Aprendizado Básico.
Sistema de tutoria interativa adaptado ao contexto ribeirinho amazônico.
Compatível com Raspberry Pi e computadores comuns (roda 100% offline).
"""

import json
import os
import time
from datetime import datetime
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from conteudo import LICOES_LEITURA, LICOES_MATEMATICA


# ─────────────────────────────────────────────
# Configurações
# ─────────────────────────────────────────────

ARQUIVO_PROGRESSO = "progresso_usuario.json"

ESTRELAS = {
    "otimo":   "⭐⭐⭐ Excelente!",
    "bom":     "⭐⭐   Bom trabalho!",
    "regular": "⭐    Continue tentando!",
}

MENSAGENS_ACERTO = [
    "✅ Correto! Muito bem!",
    "✅ Isso mesmo! Você acertou!",
    "✅ Parabéns! Resposta certa!",
]

MENSAGENS_ERRO = [
    "❌ Não foi dessa vez. Tente de novo!",
    "❌ Quase lá! Pense com calma.",
    "❌ Errou, mas não desanima!",
]


# ─────────────────────────────────────────────
# Gerenciamento de progresso (salvo em JSON)
# ─────────────────────────────────────────────

def carregar_progresso():
    if os.path.exists(ARQUIVO_PROGRESSO):
        with open(ARQUIVO_PROGRESSO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "nome": None,
        "leitura": {"nivel_atual": 1, "acertos_totais": 0, "tentativas_totais": 0},
        "matematica": {"nivel_atual": 1, "acertos_totais": 0, "tentativas_totais": 0},
        "sessoes": []
    }


def salvar_progresso(progresso):
    with open(ARQUIVO_PROGRESSO, "w", encoding="utf-8") as f:
        json.dump(progresso, f, ensure_ascii=False, indent=2)


# ─────────────────────────────────────────────
# Utilitários de interface
# ─────────────────────────────────────────────

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def linha(char="─", tamanho=50):
    print(char * tamanho)


def pausar(msg="Pressione ENTER para continuar..."):
    input(f"\n{msg}")


def cabecalho(titulo):
    limpar_tela()
    linha("═")
    print(f"  🌊 ASSISTENTE RIBEIRINHO — {titulo.upper()}")
    linha("═")
    print()


def exibir_estrelas(acertos, total):
    pct = acertos / total if total > 0 else 0
    if pct >= 0.8:
        print(f"\n  {ESTRELAS['otimo']}  ({acertos}/{total} corretas)")
    elif pct >= 0.5:
        print(f"\n  {ESTRELAS['bom']}  ({acertos}/{total} corretas)")
    else:
        print(f"\n  {ESTRELAS['regular']}  ({acertos}/{total} corretas)")


# ─────────────────────────────────────────────
# Motor de lição
# ─────────────────────────────────────────────

def executar_licao(licoes, area, nivel, progresso):
    """
    Executa uma lição completa com perguntas de múltipla escolha.
    Retorna o número de acertos.
    """
    licao = licoes.get(nivel)
    if not licao:
        print("  ⚠️  Nível não encontrado.")
        return 0

    cabecalho(f"{area} — Nível {nivel}: {licao['titulo']}")

    # Exibe texto de contexto da lição
    if "texto" in licao:
        print("  📖 Leia com atenção:\n")
        print(f"  \"{licao['texto']}\"\n")
        linha()
    elif "contexto" in licao:
        print(f"  📌 {licao['contexto']}\n")
        linha()

    pausar("Pressione ENTER quando estiver pronto para as perguntas...")

    acertos = 0
    perguntas = licao["perguntas"]

    for i, pergunta in enumerate(perguntas, 1):
        cabecalho(f"{area} — Nível {nivel} — Pergunta {i}/{len(perguntas)}")

        print(f"  ❓ {pergunta['enunciado']}\n")
        opcoes = pergunta["opcoes"]

        for j, opcao in enumerate(opcoes, 1):
            print(f"     {j}. {opcao}")

        tentativas = 0
        respondeu = False

        while not respondeu:
            print()
            entrada = input("  Sua resposta (número ou texto): ").strip()

            # Aceita número ou texto
            resposta_usuario = None
            if entrada.isdigit():
                idx = int(entrada) - 1
                if 0 <= idx < len(opcoes):
                    resposta_usuario = opcoes[idx]
            else:
                resposta_usuario = entrada

            if resposta_usuario is None:
                print("  ⚠️  Por favor, escolha uma das opções.")
                continue

            tentativas += 1

            if resposta_usuario.lower() == pergunta["resposta"].lower():
                print(f"\n  {MENSAGENS_ACERTO[i % len(MENSAGENS_ACERTO)]}")
                acertos += 1
                respondeu = True
            else:
                print(f"\n  {MENSAGENS_ERRO[tentativas % len(MENSAGENS_ERRO)]}")
                if tentativas == 1:
                    print(f"  💡 Dica: {pergunta['dica']}")
                elif tentativas >= 2:
                    print(f"  ✏️  A resposta correta era: {pergunta['resposta']}")
                    respondeu = True

        pausar()

    # Resultado da lição
    cabecalho(f"Resultado — {area} Nível {nivel}")
    exibir_estrelas(acertos, len(perguntas))

    # Atualiza progresso
    area_key = "leitura" if area == "Leitura" else "matematica"
    progresso[area_key]["acertos_totais"] += acertos
    progresso[area_key]["tentativas_totais"] += len(perguntas)

    # Avança de nível se acertou >= 70%
    nivel_max = max(licoes.keys())
    if acertos / len(perguntas) >= 0.7 and nivel < nivel_max:
        nivel_proximo = nivel + 1
        progresso[area_key]["nivel_atual"] = nivel_proximo
        print(f"\n  🎉 Você avançou para o Nível {nivel_proximo}!")

    salvar_progresso(progresso)
    pausar()
    return acertos


# ─────────────────────────────────────────────
# Menu de área
# ─────────────────────────────────────────────

def menu_area(area, licoes, chave_progresso, progresso):
    while True:
        cabecalho(area)
        nivel_atual = progresso[chave_progresso]["nivel_atual"]
        acertos = progresso[chave_progresso]["acertos_totais"]
        tentativas = progresso[chave_progresso]["tentativas_totais"]

        print(f"  👤 {progresso['nome']}   |   Nível atual: {nivel_atual}")
        pct = int(acertos / tentativas * 100) if tentativas > 0 else 0
        print(f"  📊 Aproveitamento total: {acertos}/{tentativas} ({pct}%)\n")
        linha()

        print("  1. Fazer a lição do nível atual")
        print("  2. Escolher outro nível")
        print("  3. Ver todos os níveis disponíveis")
        print("  0. Voltar ao menu principal")
        print()
        opcao = input("  Opção: ").strip()

        if opcao == "1":
            executar_licao(licoes, area, nivel_atual, progresso)

        elif opcao == "2":
            niveis = list(licoes.keys())
            print(f"\n  Níveis disponíveis: {niveis}")
            try:
                n = int(input("  Qual nível? ").strip())
                if n in niveis:
                    executar_licao(licoes, area, n, progresso)
                else:
                    print("  ⚠️  Nível inválido.")
                    pausar()
            except ValueError:
                print("  ⚠️  Digite um número.")
                pausar()

        elif opcao == "3":
            cabecalho(f"Níveis de {area}")
            for n, licao in licoes.items():
                status = "✅" if n < nivel_atual else ("▶️ " if n == nivel_atual else "🔒")
                print(f"  {status} Nível {n}: {licao['titulo']}")
            pausar()

        elif opcao == "0":
            break


# ─────────────────────────────────────────────
# Menu principal
# ─────────────────────────────────────────────

def menu_principal():
    progresso = carregar_progresso()

    # Cadastro do nome na primeira vez
    if not progresso["nome"]:
        cabecalho("Bem-vindo!")
        print("  Olá! Sou o Assistente Ribeirinho. 🌊")
        print("  Vou te ajudar a aprender leitura e matemática!\n")
        nome = input("  Qual é o seu nome? ").strip()
        progresso["nome"] = nome if nome else "Estudante"
        progresso["sessoes"].append(str(datetime.now()))
        salvar_progresso(progresso)

    while True:
        cabecalho("Menu Principal")
        print(f"  Olá, {progresso['nome']}! O que vamos estudar hoje?\n")
        linha()
        print("  1. 📖 Leitura e Linguagem")
        print("  2. 🔢 Matemática")
        print("  3. 📊 Ver meu progresso")
        print("  0. Sair")
        print()
        opcao = input("  Opção: ").strip()

        if opcao == "1":
            menu_area("Leitura", LICOES_LEITURA, "leitura", progresso)

        elif opcao == "2":
            menu_area("Matemática", LICOES_MATEMATICA, "matematica", progresso)

        elif opcao == "3":
            cabecalho("Meu Progresso")
            print(f"  👤 Nome: {progresso['nome']}")
            print(f"  📅 Sessões: {len(progresso['sessoes'])}\n")

            for area, chave in [("📖 Leitura", "leitura"), ("🔢 Matemática", "matematica")]:
                d = progresso[chave]
                pct = int(d["acertos_totais"] / d["tentativas_totais"] * 100) if d["tentativas_totais"] > 0 else 0
                print(f"  {area}")
                print(f"     Nível atual: {d['nivel_atual']}")
                print(f"     Acertos: {d['acertos_totais']}/{d['tentativas_totais']} ({pct}%)\n")
            pausar()

        elif opcao == "0":
            cabecalho("Até logo!")
            print(f"  Até a próxima, {progresso['nome']}! Continue estudando! 🌊\n")
            break


# ─────────────────────────────────────────────
# Ponto de entrada
# ─────────────────────────────────────────────

if __name__ == "__main__":
    menu_principal()
