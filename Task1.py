# Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


def sumNumbers (number):
    sum = 0
    for i in number:
        if i.isdigit():
            sum += int(i)
    print(sum)

num = input ('Введите вещественное число: ')
sumNumbers (num)
