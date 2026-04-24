# ──────────────────────────────────────────────────────────
#  EducaNorte / Assistente Ribeirinho — Dockerfile
#  Serve apenas o servidor web (web/app.py + Waitress)
#  Módulos de voz (pyttsx3/vosk) e GUI (tkinter) são
#  ignorados aqui — eles rodam localmente no Raspberry Pi.
# ──────────────────────────────────────────────────────────

FROM python:3.12-slim

# Metadados
LABEL maintainer="PET-Projeto Ribeirinho"
LABEL description="Assistente Ribeirinho — Servidor Web Educacional"

# ── Variáveis de ambiente ──────────────────────────────────
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

WORKDIR /app

# ── Dependências do sistema ────────────────────────────────
# (somente o mínimo para Flask + Waitress)
RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc \
    && rm -rf /var/lib/apt/lists/*

# ── Dependências Python ────────────────────────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Código da aplicação ────────────────────────────────────
COPY . .

# ── Porta exposta ──────────────────────────────────────────
EXPOSE 5000

# ── Ponto de entrada ───────────────────────────────────────
# Roda direto pelo Waitress (sem depender do bloco __main__)
CMD ["python", "-m", "waitress", "--host=0.0.0.0", "--port=5000", "--threads=8", "web.app:app"]
