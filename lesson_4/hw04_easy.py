__author__ = 'Барсуков Сергей Николаевич'

import random

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
print("Урок 4.\nПростые задачи.")
print("=" * 50, "\nЗадача 1.\n")

listSize = 5
defaultList = [random.randint(1, 100) for _ in range(listSize)]
quadList = [el ** 2 for el in defaultList]

print(f"defaultList: {defaultList}")
print(f"quadList:    {quadList}")

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
print("=" * 50, "\nЗадача 2.\n")

fruitList_1 = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']
fruitList_2 = ['abc', 'def', 'eee', 'dbe', 'aaa', 'fac']

crossList = [cross for cross in fruitList_1 if cross in fruitList_2]

print(f'fruitList_1: {fruitList_1}')
print(f'fruitList_2: {fruitList_2}')
print(f'crossList:   {crossList}')

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
print("=" * 50, "\nЗадача 3.\n")

defaultList = [-20, 28, 76, -54, 42, 91, 78, 73, -87, 76]

customList = [val for val in defaultList if val % 3 == 0 and val > 0 and val % 4 != 0]

print(f'defaultList: {defaultList}')
print(f'customList:  {customList}')