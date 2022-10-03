# Задайте список из n чисел последовательности 
# (1+1/n)^n и выведите на экран их сумму.

def sequence (N):
    array = []
    n = 1
    sum = 0
    for i in range (1, N + 1):
        num = (1+1/n)**n
        sum += num
        array.append(num)
        n += 1
    print (f'Сумма элементов последовательности = {sum}')
    return array

num = int (input ('Введите натуральное число: '))
array = sequence (num)
print (array)