# 2. Напишите программу, которая принимает на вход
# число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n


N = int(input("Введите число: "))
result = []

for i in range(N):
    result.append(fact(i + 1))

print(result)
