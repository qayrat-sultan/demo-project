import logging

import requests

from celery import shared_task
from django.conf import settings


@shared_task
def send_message_to_telegram(text, chat_id):
    try:
        data = {
            "chat_id": str(chat_id),
            "text": text,
        }
        resp = requests.post(
            f'https://api.telegram.org/bot{str(settings.TELEGRAM_BOT_TOKEN)}/sendMessage',
            data=data)
        if resp.status_code not in [200, 201]:
            logging.error('Error sending message. Error body: {}'.format(resp.json()))

    finally:
        logging.info(f"Sending expiration notification to user: {chat_id}")
