import requests
import time
import random

# 🔑 Твой токен бота
TOKEN = "8122323844:AAEiqjDggd5ZJDhkEwgzswyKZT5CUsWwo0U"

# 📡 URL API Telegram
URL = f"https://api.telegram.org/bot{TOKEN}"

# 🔮 Список предсказаний
predictions = [
    "Сегодня твой день!",
    "Ожидай приятного сюрприза.",
    "Лучше не рисковать сегодня.",
    "Интуиция тебя не подведёт.",
    "Скоро появится интересная возможность.",
    "Отдохни — и решение придёт само.",
    "Ты сильнее, чем думаешь."
]

# 🔁 Получаем обновления (сообщения от пользователей)
def get_updates(offset=None):
    params = {"timeout": 100, "offset": offset}
    response = requests.get(URL + "/getUpdates", params=params)
    return response.json()

# 📤 Отправляем сообщение
def send_message(chat_id, text):
    params = {"chat_id": chat_id, "text": text}
    requests.get(URL + "/sendMessage", params=params)

# ▶️ Основной цикл
def main():
    print("Бот запущен...")
    offset = None

    while True:
        updates = get_updates(offset)
        if "result" in updates:
            for update in updates["result"]:
                offset = update["update_id"] + 1
                message = update.get("message", {})
                chat_id = message.get("chat", {}).get("id")
                text = message.get("text", "").strip().lower()

                if chat_id and text:
                    if text == "/start":
                        send_message(chat_id, "Привет! Напиши /predict, и я скажу тебе что-то интересное ✨")
                    elif text == "/predict":
                        prediction = random.choice(predictions)
                        send_message(chat_id, f"🔮 {prediction}")
                    else:
                        send_message(chat_id, "Я знаю только /start и /predict 🪄")

        time.sleep(1)

if __name__ == "__main__":
    main()
