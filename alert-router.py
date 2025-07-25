import os  # Usado para acessar variáveis de ambiente do sistema

# Importa a biblioteca para envio de mensagens via Webhook no Discord
from discord_webhook import DiscordWebhook, DiscordEmbed

# FastAPI para criar a API REST
from fastapi import FastAPI

# Pydantic para validar e tipar os dados que chegam via POST
from pydantic import BaseModel

# Tipagem para listas
from typing import List


# Captura a URL do Webhook do Discord da variável de ambiente
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# Instancia a aplicação FastAPI
app = FastAPI()

# Cria um objeto Webhook com a URL do Discord
webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL)


# Modelo Pydantic que representa uma única estrutura de alerta
class Alert(BaseModel):
    annotations: dict  # Ex: {"description": "Servidor fora do ar"}
    labels: dict       # Ex: {"severity": "critical", "alertname": "InstanceDown"}

# Modelo Pydantic que representa a lista de alertas (formato esperado no POST)
class Alerts(BaseModel):
    alerts: List[Alert]


# Cria um payload de embed para o Discord a partir dos dados do alerta
def get_embed_payload(severity: str, alertname: str, description: str) -> DiscordEmbed:
    return DiscordEmbed(
        title=f"[{severity.upper()}] - {alertname}",  # Exibe severidade e nome do alerta
        description=description,                      # Mensagem do alerta
        color="ff0000",                               # Cor vermelha no embed (em hex)
    )


# Função que monta e envia o embed via Webhook para o Discord
def send_discord_webhook(severity: str, alertname: str, description: str):
    embed = get_embed_payload(severity, alertname, description)  # Cria o embed
    webhook.add_embed(embed)  # Adiciona o embed ao objeto webhook
    webhook.execute()         # Envia a mensagem ao Discord


# Endpoint GET básico para teste (ex: /)
@app.get("/")
def read_root():
    return {"Hello": "World"}  # Apenas retorna um JSON simples


# Endpoint POST que recebe alertas e envia cada um como mensagem para o Discord
@app.post("/alerts")
def send_discord_webhook_post(alert: Alerts):
    for alert in alert.alerts:  # Itera sobre todos os alertas enviados no corpo da requisição
        severity = alert.labels.get("severity")         # Ex: "critical"
        alertname = alert.labels.get("alertname")       # Ex: "DiskFull"
        description = alert.annotations.get("description")  # Ex: "Disco acima de 90%"

        send_discord_webhook(severity, alertname, description)  # Envia o alerta ao Discord

    return alert  # Retorna os dados recebidos como resposta
