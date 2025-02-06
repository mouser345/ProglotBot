import os
import requests

def send_signal_to_telegram(message):
    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("✅ Сообщение успешно отправлено.")
    else:
        print(f"❌ Ошибка отправки: {response.json()}")

# Генерация и отправка тестового сообщения
signal_message = "✅ Тестовое сообщение от бота на Render: Проверка успешна!"
send_signal_to_telegram(signal_message)
