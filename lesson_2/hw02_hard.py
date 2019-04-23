# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
print("Урок 2.\nСложные задачи.")
print("="*50, "\nЗадача 1.\n\
    Решение уравнения\n")

equation = 'y = -12x + 11111140.2121'
x = 2.5

MathSigns = {'+', '-', '='}
EqParts = equation.split(' ')

ConstSign = EqParts[3]
XSign = '+'
if not EqParts[2][0].isnumeric():
    XSign = '-'

XNum = ''
for xn in EqParts[2]:
    if xn.isnumeric():
        XNum += xn

x_val = x * float(XNum)
if XSign == '-':
    x_val *= -1

const_val = float(EqParts[4])
if ConstSign == '-':
    const_val *= -1

y_val = x_val + const_val

print(f'Необходимо решить уравнение:\n{equation}')
print(f'Ответ, при x = {x}:\ny = {y_val}')

# for eq in EqParts:
#     if eq in MathSigns:
#         EqParts.remove(eq)

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
print("="*50, "\nЗадача 3.\n\
    'Перевёрнутая башня'\n")

in_flat = int(input('Введите номер квартиры:'))

QuadPack_Num = 0                                                        # Номер квадрата
Float_QuadPack_End = 0                                                  # Последняя квартира в квадрате
Floor = 0

while(Float_QuadPack_End < in_flat):
    Floor += QuadPack_Num                                               # Этажей за предыдущие квадраты
    QuadPack_Num += 1
    Float_QuadPack_End += QuadPack_Num ** 2

Float_BeforeQuadPack_End = Float_QuadPack_End - QuadPack_Num ** 2       # Квартира до начала квадрата
FlatNumInQuad = in_flat - Float_BeforeQuadPack_End                      # Квартира относительно начала квадрата
FloorShiftInQuad = FlatNumInQuad // QuadPack_Num                        # Этаж относительно начала квадрата
Float_FromLeft = FlatNumInQuad % QuadPack_Num

if Float_FromLeft:
    FloorShiftInQuad += 1
else:
    Float_FromLeft = QuadPack_Num

Floor += FloorShiftInQuad

print(f'Ответ: {Floor}, {Float_FromLeft}')
