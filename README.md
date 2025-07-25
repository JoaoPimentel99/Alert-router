 🚨 Alert to Discord Webhook (FastAPI)

Este projeto é uma API simples construída com **FastAPI** que recebe **alertas em formato JSON** (como os enviados pelo Prometheus Alertmanager) e os envia como **embeds personalizados** para um **canal do Discord via Webhook**.

 📌 Funcionalidades

- ✅ Recebe múltiplos alertas via HTTP POST
- 📦 Suporte a `annotations` e `labels` no payload
- 🎨 Formata os alertas como embeds no Discord
- 🧩 Integração fácil com sistemas de monitoramento (ex: Alertmanager)

---

 🚀 Como executar

 1. Clonar o repositório
    bash
    git clone https://github.com/seu-usuario/alert-discord-fastapi.git
    cd alert-discord-fastapi

2. Instalar as dependências
   
   pip install -r requirements.txt

3. Definir a variável de ambiente
   Configure a URL do seu webhook do Discord:  

   Linux/macOS

   export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."

   Windows (CMD)
   
   set DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...

📫 Endpoints

    GET /
    Verificação simples para saber se a API está rodando.
    
    curl http://localhost:8000/



