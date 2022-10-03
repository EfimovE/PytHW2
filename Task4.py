# Задайте список из N элементов, заполненных числами из 
# промежутка [-N, N]. Найдите произведение элементов на указанных 
# позициях. Позиции хранятся в файле file.txt в 
# одной строке одно число.

import random

number = int (input("Введите число N и нажмите Enter: "))
array = []
for i in range (number):
    array.append (random.randint(- number, number + 1))
print (array)

arrayTxt = []
with open ('file.txt', 'r') as data:
    arrayTxt = data.read().split('\n')
print (arrayTxt)
multiplication = array[int(arrayTxt[0])] * array[int(arrayTxt[1])]
print (f' Произведение элементов на позициях {arrayTxt[0]} и {arrayTxt[1]} равно {multiplication}')
