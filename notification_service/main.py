from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/notify")
def send_notification(message: str):
    # Example Slack webhook
    webhook_url = "https://hooks.slack.com/services/your/webhook/url"
    requests.post(webhook_url, json={"text": message})
    return {"message": "Notification sent"}

