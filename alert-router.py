import os

from discord_webhook import DiscordWebhook, DiscordEmbed
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

app = FastAPI()
webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL)

class Alert(BaseModel):
    annotations: dict
    labels: dict

class Alerts(BaseModel):
    alerts: List[Alert]


def get_embed_payload(severity: str, alertname: str, description: str) -> DiscordEmbed:
    return DiscordEmbed(
        title=f"[{severity.upper()}] - {alertname}",
        description=description,
        color="ff0000",
    )


def send_discord_webhook(severity: str, alertname: str, description: str):
    embed = get_embed_payload(severity, alertname, description)
    webhook.add_embed(embed)
    webhook.execute()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/alerts")
def send_discord_webhook_post(alert: Alerts):
    for alert in alert.alerts:
        severity = alert.labels.get("severity")
        alertname = alert.labels.get("alertname")
        description = alert.annotations.get("description")
        send_discord_webhook(severity, alertname, description)
    return alert
