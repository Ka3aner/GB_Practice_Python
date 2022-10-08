# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input("Введите число: "))
N_start = N
result = []

while not N % 2:
    result.append(2)
    N //= 2

for i in range(3, int(N ** (1 / 2)) + 1, 2):
    while not N % i:
        result.append(i)
        N //= i
    if N == 1:
        break

if N > 2:
    result.append(N)

print(f"Список простых множителей числа {N_start}: ", result)
