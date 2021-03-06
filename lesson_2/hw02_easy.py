__author__ = 'Барсуков Сергей Николаевич'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
print("Урок 2.\nПростые задачи.")
print("="*50,"\nЗадача 1.\n\
    Список фруктов.\n")

FruitList = ['яблоко', 'груша', 'персик', 'ананас']
i = 1
for f_l in FruitList:
    print(f'{i}. {f_l:>10}')
    i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print("="*50,"\nЗадача 2.\n\
    Удаление из списка 1 элемнтов списка 2.\n")

MyList_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '3']
MyList_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', '0', '3', '2']
print(f'Списки:\n1) {MyList_1}\n2) {MyList_2}')

NoMatch_Flag = 1
while NoMatch_Flag:
    for ml2 in MyList_2:
        if(ml2 in MyList_1):
            MyList_1.remove(ml2)
            NoMatch_Flag = 0

    if NoMatch_Flag:
        break
    NoMatch_Flag = 1

print(f'\nПервый список после вычитания: {MyList_1}')

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print("="*50,"\nЗадача 3.\n\
    Форматирование списка.\n")

print(f'Исходный список:\n1) {MyList_1}')
for ind, ml1 in enumerate(MyList_1):
    if not (int(ml1) % 2):
        MyList_1[ind] = str(int(ml1) / 4)
    else:
        MyList_1[ind] = str(int(ml1) * 2)

print(f'Отформатированный список:\n1) {MyList_1}')