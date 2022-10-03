# Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N.

def F (n):
    factorial = 1
    for i in range (1, n + 1):
        factorial *= i
        print (factorial, end= " ")

N = int (input ('Введите натуральное число: '))
F (N)

