# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def dec_to_bin(num):
    if num > 0:
        dec_to_bin(num // 2)  
    print(num % 2, end='')


n = int(input("Введите число: "))

print(f'{n} => ', end='')
dec_to_bin(n)
