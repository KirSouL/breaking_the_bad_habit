import requests

from config.settings import TG_BOT_TOKEN, BOT_URL, BOT_ID


def post_send_tg_message(text, chat_id):
    """ Отправка сообщения на Телеграм"""

    params = {
        "text": text,
        "chat_id": chat_id,
    }
    return requests.get(f"{BOT_URL}{TG_BOT_TOKEN}/sendMessage", params=params)


def get_chat_id(username_tg):
    """ Получение chat_id Телеграм по username """

    response = requests.get(f"{BOT_URL}{TG_BOT_TOKEN}/getUpdates", params={"chat_id": BOT_ID})

    data = response.json()
    chat_id = None
    if data["ok"]:
        updates = data["result"]
        for update in updates:
            if "message" in update:
                if update["message"]["chat"]["username"] == username_tg[1:]:
                    chat_id = update["message"]["chat"]["id"]
    return chat_id
