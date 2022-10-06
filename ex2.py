# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst = [2, 3, 4, 5, 6] 
lst2 = [2, 3, 5, 6] 

def multiply_pair(lst):
    arr = []
    j = len(lst) - 1
    for i in range(0, len(lst)):
        arr.append(lst[i] * lst[j])
        j -= 1
        if(j <= i):
            break
        
        
    return arr

print(f'{lst} => {multiply_pair(lst)}')
print(f'{lst2} => {multiply_pair(lst2)}')



