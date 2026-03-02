import os
import shutil

# Папка для исходных файлов
source_dir = "source"
# Папка для выходных файлов
output_dir = "output"

# Убедимся, что папка output существует
os.makedirs(output_dir, exist_ok=True)

# Список для хранения строк из всех плейлистов
playlist = []

# Чтение всех файлов в папке source
for filename in os.listdir(source_dir):
    if filename.endswith(".m3u"):
        with open(os.path.join(source_dir, filename), "r", encoding="utf-8") as file:
            playlist.extend(file.readlines())

# Запись объединённого плейлиста в final.m3u
with open(os.path.join(output_dir, "final.m3u"), "w", encoding="utf-8") as outfile:
    outfile.write("#EXTM3U\n")
    outfile.writelines(playlist)
