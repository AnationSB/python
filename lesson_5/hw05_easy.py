__author__ = "Барсуков Сергей Николаевич"

import os
import sys
import hw05_module

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт
# и второй скрипт, удаляющий эти папки
print("Урок 5.\nПростые задачи.")
print("=" * 50, "\nЗадача 1.\n")

dirPath = os.path.abspath(os.path.curdir)

[hw05_module.makeDir(os.path.join(dirPath, 'dir_' + str(i + 1))) for i in range(9)]
print(f"Папки dir-dir9 созданы в директории {dirPath}")
input('Самое время проверить созданные папки, иначе они сотрутся!\nНажмите ввод, чтобы продолжить')
[hw05_module.removeDir(os.path.join(dirPath, 'dir_' + str(i + 1))) for i in range(9)]
print(f"Папки dir-dir9 удалены из директории {dirPath}")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print("=" * 50, "\nЗадача 2.\n")

print(f'В директории {dirPath} содержатся следующие папки:')
for ls in hw05_module.lsFolders(dirPath):
    print(f"{ls}")

# Задача-3:
# Напишите скрипт, создающий копию файла, из котрого запущен данный скрипт.
print("=" * 50, "\nЗадача 3.\n")
dirPath = os.path.abspath(os.path.curdir)
filePath = os.path.basename(sys.argv[0])
print(f"Скрипт запущен из файла: {filePath}\n")

for i in range(9):
    filePath = hw05_module.copyExFile(dirPath, filePath)
for i in range(3):
    filePath = hw05_module.copyExFile(dirPath, filePath)