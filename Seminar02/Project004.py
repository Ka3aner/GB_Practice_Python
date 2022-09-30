# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from math import prod

N = int(input("Введите число: "))
lst = list(range(-N, N + 1))

print(prod(
    lst[int(str)] for str in open('file.txt', "r")))
