# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci(n):
    fib1 = 0
    fib2 = 1
    lst = [0, 1]
    for i in range(2, n + 1):
        tmp = fib1 + fib2
        lst.append(tmp)
        fib1 = fib2
        fib2 = tmp
    return lst


def negafibonacci(n):
    fib1 = 0
    fib2 = 1
    lst = [0, 1]
    for i in range(2, n+1):
        tmp = fib1 - fib2
        lst.append(tmp)
        fib1 = fib2
        fib2 = tmp
    lst.reverse()
    return lst


def fullfibonacci(fib, nefib):
    lst = nefib
    if(fib[0] == 0):
        lst.extend(fib[1:])
    else:
        lst.extend(fib)
    return lst

    
num = int(input('Введите число для расчета фибоначи: '))

fib = fibonacci(num)

nega_fib = negafibonacci(num)

print(fullfibonacci(fib, nega_fib))
