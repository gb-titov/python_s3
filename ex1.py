# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lst = [2, 3, 5, 9, 3]

def sum_odd(lst):
    sum = 0
    for i in range(1, len(lst), 2):
        sum+= lst[i]
    return sum


print(f'{lst} => {sum_odd(lst)}')
