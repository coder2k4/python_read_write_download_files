import os
import shutil

import requests  # не стандартная библиотека, требуется установить

ABSOLUTE_FILE_PATH = os.path.abspath(__file__)
ABSOLUTE_DIR_PATH = os.path.dirname(ABSOLUTE_FILE_PATH)
ABSOLUTE_DOWNLOAD_DIR_PATH = os.path.join(ABSOLUTE_DIR_PATH, 'download-folder')

os.makedirs(ABSOLUTE_DOWNLOAD_DIR_PATH, exist_ok=True)

# путь до файла, который мы будем сохранять
download_file_path_small = os.path.join(ABSOLUTE_DOWNLOAD_DIR_PATH, '1.png')


url_small = 'https://images7.alphacoders.com/679/thumb-1920-679140.png'
url_large = 'https://www.radiantmediaplayer.com/media/big-buck-bunny-360p.mp4'


# имя конечного файла (url) big-buck-bunny-360p.mp4
download_file_basename = os.path.basename(url_large)
# путь куда сохраняем
download_file_path_large = os.path.join(ABSOLUTE_DOWNLOAD_DIR_PATH, download_file_basename)


# Для небольших файлов
# Запрашиваем картинку
response = requests.get(url_small, stream=True)
response.raise_for_status()  # Если статус ответа от сервера не 200 (OK) то выкидываем ошибку

# Закидываем контент в файл (запись байтов)
with open(download_file_path_small, 'wb') as file_handler:
    file_handler.write(response.content)

# Для больших файлов, загрузка частями
# при таком открытии через with requests не закрывает соединение и позволяет загружать большие файлы
with requests.get(url_large, stream=True) as response:
    with open(download_file_path_large, 'wb') as file_handler:
        shutil.copyfileobj(response.raw, file_handler)
