# 5. Реализуйте алгоритм перемешивания списка.

from random import shuffle

# Функция для заполнения листа из консоли. Не требуется в данной задачи, но пригодится в будущих проектах
def fill_list():
    result = []
    while True:
        str = input("Введите элемент листа (Нажмите 'Enter', чтобы закончить): ")
        if str == "":
            return result
        result.append(str)


lst = fill_list()
print(lst)
shuffle(lst)
print(lst)