# 🚀 Guia de Deploy — EducaNorte / Assistente Ribeirinho

## O que é o Docker?

Docker "empacota" o app com tudo que ele precisa para rodar — Python, bibliotecas, configurações — numa caixinha chamada **container**. Assim o app funciona igual em qualquer máquina ou servidor, sem problema de "no meu PC funciona".

---

## 📁 Estrutura esperada do projeto

Coloque os arquivos deste guia **dentro da pasta raiz do projeto** (`PET-Projeto 2026/`):

```
PET-Projeto 2026/
├── Dockerfile          ← novo
├── docker-compose.yml  ← novo
├── requirements.txt    ← novo
├── .dockerignore       ← novo
├── web/
│   └── app.py
├── modulo_alfabetizacao/
├── modulo_ambiental/
│   ... (demais módulos)
```

---

## 🖥️ Opção 1 — Rodar localmente com Docker

Ideal para **testes** ou rodar numa máquina da equipe.

### Pré-requisitos
- Instalar o Docker: https://docs.docker.com/get-docker/

### Comandos

```bash
# Entrar na pasta do projeto
cd "PET-Projeto 2026"

# Construir e subir o servidor
docker compose up --build

# Acessar no navegador:
# http://localhost:5000
```

Para parar: `Ctrl+C`, depois `docker compose down`

---

## ☁️ Opção 2 — Deploy na Railway (nuvem gratuita) ⭐ Recomendado

**Railway** é a forma mais fácil de colocar no ar com link público permanente.

### Passo a passo

1. Crie uma conta gratuita em https://railway.app

2. Instale o CLI:
   ```bash
   npm install -g @railway/cli
   # ou baixe o instalador no site
   ```

3. Na pasta do projeto:
   ```bash
   railway login
   railway init
   railway up
   ```

4. Pegue o link público gerado:
   ```
   https://seu-projeto.railway.app
   ```

O Railway detecta o `Dockerfile` automaticamente. ✅

### Plano gratuito
- 500 horas/mês (suficiente para testes contínuos)
- 512 MB RAM
- Link HTTPS incluso

---

## ☁️ Opção 3 — Deploy no Render (alternativa gratuita)

1. Crie conta em https://render.com
2. Clique em **New → Web Service**
3. Conecte ao repositório GitHub com o código
4. Configure:
   - **Build Command:** `docker build -t app .`
   - **Start Command:** já está no Dockerfile
   - **Port:** `5000`
5. Clique em **Deploy**

---

## ☁️ Opção 4 — VPS própria (DigitalOcean, Oracle Cloud Free, etc.)

Se quiser mais controle e performance:

```bash
# Na VPS (Ubuntu 22.04)
sudo apt update
sudo apt install docker.io docker-compose-plugin -y

# Copiar o projeto para a VPS via SCP
scp -r "PET-Projeto 2026/" usuario@ip-da-vps:~/

# Na VPS
cd "PET-Projeto 2026"
docker compose up -d   # -d = roda em segundo plano
```

Acesso: `http://IP-DA-VPS:5000`

Para HTTPS com domínio próprio, adicione Nginx + Certbot.

---

## 💾 Sobre os dados dos alunos

Os arquivos `perfis.json`, `turmas.json`, `avisos.json` são criados/atualizados pelo app em tempo real.

No `docker-compose.yml` já está configurado um **volume** para salvar esses dados fora do container:

```yaml
volumes:
  - ./dados:/app/dados
```

⚠️ **Atenção:** o `web/app.py` salva os arquivos na raiz do projeto. Se quiser que o volume funcione, ajuste os caminhos `ARQUIVO_PERFIS`, `ARQUIVO_TURMAS` etc. para apontar para `/app/dados/`:

```python
# Em web/app.py, troque:
ARQUIVO_PERFIS = os.path.join(_PARENT, "perfis.json")
# Por:
ARQUIVO_PERFIS = os.path.join(_PARENT, "dados", "perfis.json")
```

---

## 🤖 Módulo de IA (Ollama)

O módulo de IA usa o Ollama rodando localmente. Na nuvem, você tem duas opções:

**Opção A — Desativar a IA** (mais simples): o app já trata isso com `try/except`, mostrando "IA indisponível" para o aluno.

**Opção B — Rodar Ollama junto**: descomente o serviço `ollama` no `docker-compose.yml`. Requer um servidor com pelo menos **4GB de RAM** e o modelo baixado.

---

## ❓ Problemas comuns

| Erro | Solução |
|------|---------|
| `Port 5000 already in use` | Troque a porta no `docker-compose.yml`: `"8080:5000"` |
| `ModuleNotFoundError: flask` | O `requirements.txt` não foi copiado — verifique a estrutura de pastas |
| App sobe mas não abre | Verifique se o firewall permite a porta 5000 |
| Dados sumindo ao reiniciar | Configure o volume no `docker-compose.yml` |
