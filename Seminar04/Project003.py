# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from Functions import fill_list_numbers

print("Полученный список: ", lst := fill_list_numbers())

print("Полученный список уникальных элементов: ", list(set(lst)))

print("Полученный список неповторяющихся элементов: ", list(item for item in lst if lst.count(item) == 1))
