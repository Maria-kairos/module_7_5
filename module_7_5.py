import os
import time
from os.path import getsize, join, getmtime, dirname

def information(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = join(root, file)
            filetime = getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y%H:%M", time.localtime(filetime))
            filesize = getsize(filepath)
            parent_dir = dirname(filepath)
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}.')

if __name__ == '__main__':
    information('.venv')