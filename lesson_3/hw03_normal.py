__author__ = 'Барсуков Сергей Николаевич'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print("Урок 3.\nЗадачи нормальной сложности.")
print("="*50,"\nЗадача 1.\n")

def findNFibonacci(N):
    goldenRatio = (1 + 5 ** 0.5) / 2
    return int((goldenRatio ** N - (-goldenRatio) ** (-N)) / (2 * goldenRatio - 1))

def fibonacci(n,m):
    FibonacciSerieN2M = []
    for i in range(n, m):
        FibonacciSerieN2M.append(findNFibonacci(i))
    return FibonacciSerieN2M

print(fibonacci(4, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print("="*50,"\nЗадача 2.\n")

def sort_to_max(origin_list):
    for i in range(0, len(origin_list) - 1):
        for j in range(0, len(origin_list) - 1):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j] += origin_list[j + 1]
                origin_list[j + 1] = origin_list[j] - origin_list[j + 1]
                origin_list[j] -= origin_list[j + 1]
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print("="*50,"\nЗадача 3.\n")

def myFilter(func, iterable):
    iterable_mass = []
    if func == None:
        for i in iterable:
            if i:
                iterable_mass.append(i)
    else:
        for i in iterable:
            if func(i):
                iterable_mass.append(i)
    return iterable_mass

mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
zolushka = list(myFilter(lambda x: x == 'мак', mixed))
print(zolushka)
zolushka = list(filter(lambda x: x == 'мак', mixed))
print(zolushka)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print("="*50,"\nЗадача 4.\n")

def areLinesParallel(AB, CD):
    degCoef_AB = (AB[2] - AB[0]) / (AB[3] - AB[1])
    degCoef_CD = (CD[2] - CD[0]) / (CD[3] - CD[1])
    if degCoef_AB == degCoef_CD:
        return True
    else:
        return False

def areLinesSame(AB, CD):
    AB_len = ((AB[2] - AB[0]) ** 2 + (AB[3] - AB[1]) ** 2) ** 0.5
    CD_len = ((CD[2] - CD[0]) ** 2 + (CD[3] - CD[1]) ** 2) ** 0.5
    if AB_len == CD_len:
        return True
    else:
        return False

def isParallelogramm(A, B, C, D):
    if (A[0] == B[0] == C[0] == D[0]) or (A[1] == B[1] == C[1] == D[1]):
        print("Точки лежат на одной прямой")
        return 0xFFFFFFFF

    allPoints = (A, B, C, D)
    firstLine = []
    secondLine = []

    for i in range(0, 3):
        firstLine = allPoints[0] + allPoints[1 + i]
        secondLine = allPoints[-(2 + i % 2)] + allPoints[-(1 + 2* int(i == 2))]
        if areLinesSame(firstLine, secondLine) and areLinesParallel(firstLine, secondLine):
            print(f'Координаты прямых в виде ABCD {firstLine+secondLine}\nДанные точки можно соединить в параллелограмм')
            return True

    return False

# isParallelogramm([-3,11], [12,-4], [1,-7], [-14,8])
# isParallelogramm([-3,11], [1,-7], [12,-4], [-14,8])
isParallelogramm([12,-4], [-14,8], [1,-7], [-3,11])
