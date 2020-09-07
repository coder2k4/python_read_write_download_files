import os

# Получаем абсолютный путь до корневой дирректории
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Соединяем корневую дирректорию и папку txt-folder
multiple_files_dir = os.path.join(BASE_DIR, 'txt-folder')

# Создаем дирректорию, если дирректория уже существует - пропускаем (exist_ok=True)
os.makedirs(multiple_files_dir, exist_ok=True)

# генерируем диапазон от 0 до 10
multiple_txt_files = range(0, 10)

for file in multiple_txt_files:
    fname = f"{file}.txt"  # генерируем имя по диапазона
    file_path = os.path.join(multiple_files_dir, fname)  # соединиям название и путь к директории
    if os.path.exists(file_path):  # проверяем на существование файла
        print(f"Файл {fname} пропущен, уже существует")
        continue  # запускаем следующую интерацию
    with open(file_path, 'w') as f:
        f.write("Просто текст, для записи в каждый файл")
