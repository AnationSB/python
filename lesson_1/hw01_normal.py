__author__ = 'Барсуков Сергей Николаевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
print("Урок 1.\nЗадачи нормальной сложности.")
print("="*50,"\nЗадача 1.\n\
    Вывод старшей цифры числа.\n")

in_val = input("Введите произвольное число:")

i = 0
max_num = 0
while i < len(in_val):
    if int(in_val[i]) > max_num:
        max_num = int(in_val[i])
    i += 1
print("Максимальная цифра: ", max_num)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
print("="*50,"\nЗадача 2.\n\
    Поменять значения переменных местами.\n")

in_a = int(input("Введите значение переменной a:"))
in_b = int(input("Введите значение переменной b:"))

in_a += in_b
in_b  = in_a - in_b
in_a -= in_b

print("После смены значений\n\
    a = ",  in_a, "\n\
    b = ",  in_b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
import math

print("="*50,"\nЗадача 3.\n\
    Вычисление корней квадратного уравнения.\n")

print("ax² + bx + c = 0")
in_a = int(input("Введите коэффициент a: "))
in_b = int(input("Введите коэффициент b: "))
in_c = int(input("Введите коэффициент c: "))

Discriminant = (in_b**2 - 4*in_a*in_c)
if Discriminant < 0:
    print('Отрицательный дискриминант.\nРабота с мнимыми числами не поддерживается.')
else:
    Discriminant = math.sqrt(Discriminant)
    x1 = (-in_b + Discriminant) / 2*in_a
    x2 = (-in_b - Discriminant) / 2*in_a

    print("Вывод корней уравнения:\nx1 = ", x1,\
                                 "\nx2 = ", x2)