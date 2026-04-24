"""
Módulo de Voz — Assistente Ribeirinho
Síntese de voz (TTS) com pyttsx3 e reconhecimento de voz (STT) com vosk.
100% offline, compatível com Raspberry Pi.
"""

import threading
import queue
import os
import json

# ─────────────────────────────────────────────
# Síntese de voz (Text-to-Speech)
# ─────────────────────────────────────────────

try:
    import pyttsx3
    TTS_DISPONIVEL = True
except ImportError:
    TTS_DISPONIVEL = False


class SintetizadorVoz:
    """
    Fala textos em português usando pyttsx3 (offline).
    Uso: sintetizador.falar("Olá, bem-vindo!")
    """

    def __init__(self, velocidade=150, volume=1.0):
        self.ativo = False
        if not TTS_DISPONIVEL:
            print("  ⚠️  pyttsx3 não instalado. Rode: pip install pyttsx3")
            return

        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty("rate", velocidade)   # palavras por minuto
            self.engine.setProperty("volume", volume)     # 0.0 a 1.0

            # Tenta selecionar voz em português
            vozes = self.engine.getProperty("voices")
            for voz in vozes:
                if "pt" in voz.id.lower() or "brazil" in voz.name.lower() or "portuguese" in voz.name.lower():
                    self.engine.setProperty("voice", voz.id)
                    break

            self.ativo = True
        except Exception as e:
            print(f"  ⚠️  Erro ao iniciar TTS: {e}")

    def falar(self, texto: str, bloquear=True):
        """Fala o texto. bloquear=True aguarda terminar antes de continuar."""
        if not self.ativo:
            return
        try:
            self.engine.say(texto)
            if bloquear:
                self.engine.runAndWait()
        except Exception as e:
            print(f"  ⚠️  Erro no TTS: {e}")

    def parar(self):
        if self.ativo:
            try:
                self.engine.stop()
            except Exception:
                pass


# ─────────────────────────────────────────────
# Reconhecimento de voz (Speech-to-Text)
# ─────────────────────────────────────────────

try:
    from vosk import Model, KaldiRecognizer
    import sounddevice as sd
    STT_DISPONIVEL = True
except ImportError:
    STT_DISPONIVEL = False


class ReconhecedorVoz:
    """
    Captura e transcreve fala usando Vosk (offline).

    Requer:
      pip install vosk sounddevice
      Baixar modelo PT: https://alphacephei.com/vosk/models
        → vosk-model-small-pt-0.3  (40MB, ideal para Raspberry Pi)

    Uso:
      rec = ReconhecedorVoz(caminho_modelo="modelos/vosk-model-small-pt-0.3")
      texto = rec.ouvir(timeout=5)
    """

    SAMPLE_RATE = 16000

    def __init__(self, caminho_modelo: str = "modelos/vosk-model-small-pt-0.3"):
        self.ativo = False
        if not STT_DISPONIVEL:
            print("  ⚠️  vosk/sounddevice não instalados.")
            print("       Rode: pip install vosk sounddevice")
            return

        if not os.path.exists(caminho_modelo):
            print(f"  ⚠️  Modelo Vosk não encontrado em: {caminho_modelo}")
            print("       Baixe em: https://alphacephei.com/vosk/models")
            print("       Recomendado: vosk-model-small-pt-0.3")
            return

        try:
            self.model = Model(caminho_modelo)
            self.ativo = True
            print("  🎤 Reconhecimento de voz ativado!")
        except Exception as e:
            print(f"  ⚠️  Erro ao carregar modelo Vosk: {e}")

    def ouvir(self, timeout: int = 7, mensagem: str = "🎤 Fale agora...") -> str:
        """
        Grava áudio por `timeout` segundos e retorna o texto transcrito.
        Retorna string vazia se não reconhecer nada.
        """
        if not self.ativo:
            return ""

        print(f"\n  {mensagem}")
        rec = KaldiRecognizer(self.model, self.SAMPLE_RATE)
        resultado_queue = queue.Queue()

        def callback(indata, frames, time_info, status):
            rec.AcceptWaveform(bytes(indata))

        try:
            with sd.RawInputStream(
                samplerate=self.SAMPLE_RATE,
                blocksize=8000,
                dtype="int16",
                channels=1,
                callback=callback
            ):
                print(f"  ⏳ Gravando por {timeout} segundos...")
                sd.sleep(timeout * 1000)

            resultado = json.loads(rec.FinalResult())
            texto = resultado.get("text", "").strip()

            if texto:
                print(f"  📝 Você disse: \"{texto}\"")
            else:
                print("  ❌ Não entendi. Tente novamente.")

            return texto

        except Exception as e:
            print(f"  ⚠️  Erro ao gravar: {e}")
            return ""


# ─────────────────────────────────────────────
# Classe unificada de voz
# ─────────────────────────────────────────────

class ModuloVoz:
    """
    Interface unificada para TTS + STT.
    Verifica automaticamente o que está disponível.
    """

    def __init__(self, caminho_modelo_vosk: str = "modelos/vosk-model-small-pt-0.3"):
        self.tts = SintetizadorVoz()
        self.stt = ReconhecedorVoz(caminho_modelo_vosk)

    @property
    def pode_falar(self):
        return self.tts.ativo

    @property
    def pode_ouvir(self):
        return self.stt.ativo

    def falar(self, texto: str):
        self.tts.falar(texto)

    def ouvir(self, timeout: int = 7) -> str:
        return self.stt.ouvir(timeout=timeout)

    def falar_e_ouvir(self, texto: str, timeout: int = 7) -> str:
        """Fala uma pergunta e aguarda resposta de voz."""
        self.falar(texto)
        return self.ouvir(timeout=timeout)

    def status(self):
        print("\n  === Status do Módulo de Voz ===")
        print(f"  🔊 Síntese de voz (TTS):        {'✅ Ativo' if self.pode_falar else '❌ Inativo'}")
        print(f"  🎤 Reconhecimento de voz (STT): {'✅ Ativo' if self.pode_ouvir else '❌ Inativo'}")
        if not TTS_DISPONIVEL:
            print("\n  Para ativar TTS:  pip install pyttsx3")
        if not STT_DISPONIVEL:
            print("  Para ativar STT:  pip install vosk sounddevice")
            print("  Modelo PT:        https://alphacephei.com/vosk/models")


# ─────────────────────────────────────────────
# Teste rápido
# ─────────────────────────────────────────────

if __name__ == "__main__":
    voz = ModuloVoz()
    voz.status()

    if voz.pode_falar:
        voz.falar("Olá! Eu sou o Assistente Ribeirinho. Vamos aprender juntos!")

    if voz.pode_ouvir:
        resposta = voz.falar_e_ouvir("Qual é o seu nome?", timeout=5)
        if resposta:
            voz.falar(f"Olá, {resposta}! Bem-vindo ao assistente!")
