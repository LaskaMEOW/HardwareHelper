from config import TOKEN

if __name__ == "__main__":
    if TOKEN is None:
        print("Ошибка: токен не загружен")
    else:
        print("HardwareHelper бот готов к разработке")