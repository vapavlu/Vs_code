import sys
from pathlib import Path
from colorama import init, Fore

# Ініціалізація colorama для підтримки кольорового виведення в консоль
init(autoreset=True)

def display_directory_structure(directory_path, indent=''):

    # Перевірка, чи існує директорія за вказаним шляхом
    directory = Path(directory_path)
    if not directory.is_dir():
        print(Fore.RED + f"Директорія '{directory_path}' не існує або не є директорією.")
        return

    # Виведення імені директорії з зеленим кольором
    print(Fore.GREEN + indent + f"📁 {directory.name}")

    # Обробка всіх об'єктів (піддиректорій та файлів) у даній директорії
    for item in directory.iterdir():
        if item.is_dir():
            # Виведення імені піддиректорії з синім кольором
            print(Fore.BLUE + indent + "┣ 📁 " + item.name)
            # Рекурсивний виклик функції для обробки піддиректорій
            display_directory_structure(item, indent + "  ┃ ")
        else:
            # Виведення імені файлу з жовтим кольором
            print(Fore.YELLOW + indent + "┣ 📜 " + item.name)

if __name__ == "__main__":
    # Перевірка чи був переданий аргумент командного рядка з шляхом до директорії
    if len(sys.argv) != 2:
        print("Використання: python script_name.py /шлях/до/директорії")
        sys.exit(1)

    # Отримання шляху до директорії з аргументів командного рядка
    directory_path = sys.argv[1]

    # Виклик функції для відображення структури директорії
    display_directory_structure(directory_path)