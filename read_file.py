import os

# Получаем абсолютный путь до выполняемого файла
BASE_PATH = os.path.abspath(__file__)
# Получаем абсолютный путь до корневой дирректории
BASE_DIR = os.path.dirname(BASE_PATH)
# Получаем абсолютный путь до дирректории уровнем выше дирректории проекта
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Объединяем абсолютный путь до корневой дирректории + 'file-templates/email.txt'
email_txt = os.path.join(BASE_DIR, 'file-templates', 'email.txt')  # 'file-templates/email.txt'

# Открываем файл для чтения
with open(email_txt, 'r') as file_container:
    content = file_container.read()

# Выводим прочитанные данные
print(content)
