from dotenv import load_dotenv
import os

load_dotenv()  # загружаем переменные окружения
TOKEN = os.getenv("TOKEN")  # токен Telegram-бота
