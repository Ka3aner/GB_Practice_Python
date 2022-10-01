# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(N):
    if N == -2:
        return -1
    elif abs(N) == 1 or abs(N) == 2:
        return 1
    elif not N:
        return 0
    if N < 0:
        return ((-1)**(abs(N)+1))*(fib(abs(N)-1) + fib(abs(N)-2))
    else:
        return fib(N-1) + fib(N-2)


N = int(input("Введите число: "))

print(list(fib(i) for i in range(-N, N+1)))
