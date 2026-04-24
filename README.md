# 🌊 Assistente Ribeirinho

Sistema de tutoria educacional com IA local (on-device), desenvolvido para
comunidades ribeirinhas da Amazônia. Funciona **100% offline**.

---

## 🚀 Como rodar

### 1. Instalar Python 3.7+
Já vem instalado no Raspberry Pi OS e na maioria dos sistemas.

### 2. Instalar dependências obrigatórias
```bash
# tkinter (interface gráfica) — Linux/Raspberry Pi
sudo apt install python3-tk

# Nenhuma outra dependência obrigatória!
```

### 3. Instalar dependências de voz (opcional)
```bash
pip install pyttsx3          # Síntese de voz (fala)
pip install vosk sounddevice # Reconhecimento de fala

# Baixar modelo de português (40MB — ideal para Raspberry Pi):
# https://alphacephei.com/vosk/models → vosk-model-small-pt-0.3
# Extrair em: assistente_ribeirinho/modelos/vosk-model-small-pt-0.3/
```

### 4. Executar
```bash
cd assistente_ribeirinho

python iniciar.py          # Interface gráfica (padrão)
python iniciar.py --texto  # Modo terminal (sem GUI)
```

---

## 📁 Estrutura do projeto

```
assistente_ribeirinho/
│
├── iniciar.py                      ← Ponto de entrada principal
│
├── modulo_alfabetizacao/
│   ├── main.py                     ← Motor de lições (modo terminal)
│   └── conteudo.py                 ← Banco de lições e perguntas
│
├── modulo_voz/
│   └── voz.py                      ← TTS (pyttsx3) + STT (vosk)
│
├── gui/
│   └── interface.py                ← Interface gráfica (tkinter)
│
├── modelos/                        ← Modelos de IA (criado manualmente)
│   └── vosk-model-small-pt-0.3/   ← Modelo de voz PT (baixar separado)
│
└── progresso_usuario.json          ← Salvo automaticamente
```

---

## 🧠 Arquitetura

```
┌─────────────────────────────────────────────┐
│              iniciar.py                     │
│   (detecta modo: GUI ou terminal)           │
└──────────────┬──────────────────────────────┘
               │
    ┌──────────┴──────────┐
    │                     │
┌───▼────────┐   ┌────────▼────────┐
│ gui/       │   │ modulo_         │
│ interface  │   │ alfabetizacao/  │
│ .py        │   │ main.py         │
│ (tkinter)  │   │ (terminal)      │
└───┬────────┘   └────────┬────────┘
    │                     │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │  conteudo.py        │
    │  (banco de lições)  │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │  modulo_voz/voz.py  │
    │  (TTS + STT)        │
    └─────────────────────┘
```

---

## 📖 Módulos disponíveis

| Módulo | Conteúdo | Status |
|--------|----------|--------|
| Alfabetização | Vogais, sílabas, leitura | ✅ Pronto |
| Matemática | Contagem, números, problemas | ✅ Pronto |
| Ed. Ambiental | Sustentabilidade ribeirinha | 🔜 Em breve |
| Saúde | Dicas preventivas | 🔜 Em breve |
| Cultura | Tradições ribeirinhas | 🔜 Em breve |

---

## 🍓 Configuração no Raspberry Pi

```bash
# Instalar dependências no Raspberry Pi OS
sudo apt update
sudo apt install python3-tk python3-pip

pip3 install pyttsx3 vosk sounddevice

# Rodar na inicialização (opcional)
# Adicionar ao /etc/rc.local:
cd /home/pi/assistente_ribeirinho && python3 iniciar.py &
```

### Recomendações de hardware
| Componente | Mínimo | Recomendado |
|------------|--------|-------------|
| Raspberry Pi | 3B+ (1GB RAM) | 4B (2GB RAM) |
| Armazenamento | 8GB SD | 16GB SD |
| Tela | Qualquer HDMI | Touchscreen 7" oficial |
| Microfone | USB simples | USB com cancelamento de ruído |
| Energia | Carregador 5V/2.5A | + Painel solar 10W |

---

## ➕ Como adicionar mais lições

Edite `modulo_alfabetizacao/conteudo.py` seguindo o padrão:

```python
LICOES_LEITURA[4] = {
    "titulo": "Nome do nível",
    "texto": "Texto para leitura...",
    "perguntas": [
        {
            "enunciado": "Pergunta aqui?",
            "opcoes": ["A", "B", "C", "D"],
            "resposta": "B",
            "dica": "Dica para o aluno."
        }
    ]
}
```

---

## 📋 Roadmap

- [x] Motor de lições adaptativo
- [x] Interface gráfica touchscreen
- [x] Síntese de voz offline (TTS)
- [x] Reconhecimento de voz offline (STT)
- [ ] Módulo de educação ambiental
- [ ] Módulo de saúde
- [ ] Módulo de cultura ribeirinha
- [ ] Suporte a múltiplos perfis de usuário
- [ ] Integração com modelo de linguagem leve (TinyLlama/Phi-2)
- [ ] Geração dinâmica de exercícios com IA
