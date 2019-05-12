#!/usr/bin/python3
#encoding: utf-8
__author__ = "Барсуков Сергей Николаевич"

import sys
import os
import re

import hw05_module

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей дирректории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Посмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа спрашивает название папки 
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

def printHelp(*fooArg):
    print('=' * 50)
    print('help - получить справку.')
    print('cd <Путь директории> - перейти в папку.')
    print('ls - посмотреть содержимое текущей папки.')
    print('cp <Путь директории> <Путь к файлу> - копировать в указанную директорию файл.')
    print('rmdir <Путь директории> - удалить папку.')
    print('mkdir <Путь директории> - создать папку.')
    print('exit - выйти из утилиты.')
    print('=' * 50)


print(f'Текущая директория {os.path.abspath(os.curdir)}')

try:
    arg = sys.argv[1]
except IndexError:
    arg = None
    print("Нет ключа. Для дополнительной информации воспользуйтесь help.")

try:
    dirName = sys.argv[2]
except IndexError:
    dirName = None

try:
    filePath = sys.argv[3]
except:
    filePath = None

args = {
    "help": [printHelp, None],
    "cd": [hw05_module.changeDir, dirName],
    "ls": [hw05_module.lsFolders, os.curdir],
    "rmdir": [hw05_module.removeDir, dirName],
    "mkdir": [hw05_module.makeDir, dirName],
    "cp": [hw05_module.copyExFile, dirName, filePath],
    "exit": [exit, None]
}

if arg:
    containsCmd = args.get(arg)
    if containsCmd:
        if containsCmd == args.get('cp'):
            dbgOut = args[arg][0](args[arg][1], args[arg][2])
        else:
            dbgOut = args[arg][0](args[arg][1])
    else:
        print('Ключ неверный')

printHelp()
while True:
    print(f'Текущая директория {os.path.abspath(os.curdir)}')
    inCmd = input('--> ') + ' '
    inCmd = re.split(' ', inCmd)
    if inCmd[1] == '':
        inCmd[1] = None
    if args.get(inCmd[0]):
        dbgOut = args[inCmd[0]][0](inCmd[1])
    else:
        print('Нет запрашиваемой команды.')
