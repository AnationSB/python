#!/usr/bin/python3
#encoding: utf-8
__author__ = "Барсуков Сергей Николаевич"

import os
import re
import sys
import shutil

ans_yes = ['yes', 'y']
ans_no = ['no', 'n']

def makeDir(path):
    """
    Making directory function with interactive ask for rewrite.

    Params: path.

    Ret_val: 0 - directory created. 1 - old directory prefered.
    """
    rewriteCmd = 0
    
    try:
        newDir = os.path.join(os.getcwd(), path)
        os.mkdir(newDir)
    except FileExistsError:
        while not rewriteCmd in ans_yes + ans_no:
            rewriteCmd = input(f"{newDir} уже существует.\nПерезаписать? [y/n]\n").lower()
    except TypeError:
        print('Не указана директория.')
    except PermissionError:
        print('Ошибка доступа.')
    if rewriteCmd in ans_yes:
        shutil.rmtree(path)
        os.mkdir(path)
        print(f"{path} перезаписан.")
    if rewriteCmd in ans_no:
        print(f"{path} остается без изменений.")
        return 1 

    return 0

def removeDir(path):
    """
    Remove directory function.

    Params: path.

    Ret_val: 0 - directory removed. 1 - no such directory.
    """

    try:
        shutil.rmtree(os.path.abspath(path))
    except TypeError:
        print(f"{path} не существует.")
        return 1
    except PermissionError:
        print('Ошибка доступа.')
        return 1
    return 0

def lsFolders(dirPath):
    """
    List folders in directory.

    Params: dirPath.
    """

    if not dirPath:
        dirPath = os.curdir

    try:
        ls = os.listdir(dirPath)
    except FileNotFoundError:
        print("Нет запрашиваемой директории.")
        return

    lsAbsPath = []
    for i in ls:
        lsAbsPath.append(os.path.join(dirPath, i))
    lsDir = (list(filter(lambda x: os.path.isdir(x), lsAbsPath)))
    
    j = 0
    for i in lsDir:
        lsDir[j] = os.path.basename(i)
        print(lsDir[j])
        j += 1
    return lsDir

def copyExFile(dirPath, filePath=os.path.basename(sys.argv[0])):
    """
    Copy executable script to new directory.

    Params: dirPath - new directory.

    filePath - name of executable file.

    Returns name of file copy.
    """

    baseName, extName = os.path.splitext(filePath)
    nextFreeCopyNum = 1
    namePattern = r'(.+)[(](\d+)[)]'
    copyNum = re.findall(namePattern, baseName)
    def getNextName(copyInc=''):
         return re.sub(namePattern, r'\1(' + str(copyInc) + ')', baseName)

    if copyNum: # Копируемый файл является копией
        nextFreeCopyNum = str(int(copyNum[0][1]) + 1)
        baseName = getNextName(nextFreeCopyNum)
    else: # Нет других копий
        baseName += r'(0)'

    newFileName = baseName + extName
    newFilePath = os.path.join(dirPath, newFileName)

    while os.path.exists(newFilePath):
        nextFreeCopyNum = int(nextFreeCopyNum) + 1
        baseName = getNextName(nextFreeCopyNum)

        newFileName = baseName + extName
        newFilePath = os.path.join(dirPath, newFileName)
    try:
        shutil.copyfile(filePath, newFilePath)
    except NotADirectoryError:
        print('В параметре директории указана не директория.')
        return 'ERROR'
    print(f'Файл скопирован в {newFileName}')
    return newFileName

def changeDir(dirPath):
    '''
    Change current directory.

    Params: dirPath - new directory.

    Returns new directory path. [None if error]
    '''
    try:
        foo = os.chdir(os.path.abspath(dirPath))
        return os.path.abspath(dirPath)
    except TypeError:
        print('Невозможно сменить директорию, она неуказана.')
    except OSError:
        print('Указана несуществующая директория.')
    return None
