"""
Ponto de entrada principal — Assistente Ribeirinho
Executa a interface gráfica com suporte opcional a voz.

Uso:
    python iniciar.py          → Interface gráfica (padrão)
    python iniciar.py --texto  → Modo terminal (sem GUI)
"""

import sys
import os

# ─────────────────────────────────────────────
# Verifica dependências e orienta o usuário
# ─────────────────────────────────────────────

def verificar_dependencias():
    ausentes = []

    # tkinter (geralmente já vem com Python)
    try:
        import tkinter
    except ImportError:
        ausentes.append(("tkinter", "sudo apt install python3-tk  (Linux/Raspberry Pi)"))

    # pyttsx3 (voz - opcional)
    try:
        import pyttsx3
    except ImportError:
        print("  ℹ️  Voz (TTS) não disponível. Para ativar: pip install pyttsx3")

    # vosk (STT - opcional)
    try:
        import vosk
    except ImportError:
        print("  ℹ️  Reconhecimento de fala não disponível.")
        print("       Para ativar: pip install vosk sounddevice")
        print("       Modelo PT:   https://alphacephei.com/vosk/models")

    if ausentes:
        print("\n  ⚠️  Dependências obrigatórias faltando:")
        for pkg, instrucao in ausentes:
            print(f"     {pkg}: {instrucao}")
        print()
        sys.exit(1)


# ─────────────────────────────────────────────
# Inicialização
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("\n  🌊 Assistente Ribeirinho — Iniciando...\n")
    verificar_dependencias()

    modo_texto = "--texto" in sys.argv

    if modo_texto:
        # Modo terminal
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), "modulo_alfabetizacao"))
        from modulo_alfabetizacao.main import menu_principal
        menu_principal()

    else:
        # Modo gráfico
        sys.path.insert(0, os.path.dirname(__file__))
        from gui.interface import AssistenteRibeirinho
        app = AssistenteRibeirinho()
        app.rodar()
