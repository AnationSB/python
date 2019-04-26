__author__ = 'Барсуков Сергей Николаевич'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
print("Урок 3.\nПростые задачи.")
print("="*50,"\nЗадача 1.\n")

def my_round(number, ndigits):
    exactness = 10 ** (ndigits)
    more_exact = (number * 10 * exactness) % 10
    number = int(number * exactness)
    if more_exact < 5:
        number = float(number / exactness)
    else:
        number = float((number + 1) / exactness)
    return number

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print("="*50,"\nЗадача 2.\n")

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)

    if len(ticket_number) % 2:
        print("Билет имеет нечетное количество цифр")
        return 0xdead

    left_side = 0
    right_side = 0
    for i in range(0, int(len(ticket_number) / 2)):
        left_side += int(ticket_number[i])
        right_side += int(ticket_number[-(i + 1)])

    print(f"DEBUG out:\n{left_side}\n{right_side}")
    if left_side == right_side:
        print("Билет счастливый!")
        return True
    else:
        print("Это обычный билет.")
        return False
    return 0xe0f

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

#======================================================