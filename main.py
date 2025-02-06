import requests
import os

# Параметры Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def request_signal():
    # Запрос на генерацию сигнала через OpenAI API
    response = requests.post("https://api.openai.com/v1/chat/completions", json={
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Ты генерируешь торговые сигналы."},
            {"role": "user", "content": "Сформируй сигнал для пары BTC/USDT."}
        ]
    }, headers={
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
    })

    # Обработка ответа
    if response.status_code == 200:
        data = response.json()
        message_content = data['choices'][0]['message']['content']
        return message_content
    else:
        print(f"Ошибка API: {response.json()}")
        return "❌ Не удалось получить сигнал."

def send_to_telegram(message):
    # Отправка сообщения в Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(url, json={"chat_id": CHAT_ID, "text": message})

    if response.status_code == 200:
        print("✅ Сообщение успешно отправлено.")
    else:
        print(f"❌ Ошибка отправки: {response.json()}")

# Генерация сигнала и его отправка
signal_message = request_signal()  # Запрос сигнала
send_to_telegram(signal_message)   # Отправка сообщения в Telegram
