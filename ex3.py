# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов

lst = [1.1, 1.2, 3.1, 5, 10.01] 

def get_min_max_of_fract(lst):
    min = 0
    max = 0
    for i in lst:
        cur = i % 1
        if cur > max:
            max = cur
        elif cur < min:
            min = cur
    return max - min

print(f'{lst} = > {get_min_max_of_fract(lst)}')        