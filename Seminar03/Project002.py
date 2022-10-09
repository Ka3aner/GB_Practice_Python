# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Функция заполнения листа c проверкой на число
def fill_list():
    result = []
    while True:
        string = input("Введите элемент листа (Нажмите 'Enter', чтобы закончить): ")
        if string.isdigit():
            result.append(int(string))
        elif string.replace(".", "", 1).isdigit():
            result.append(float(string))
        elif string:
            print("Введено не число. Строка не попала в лист")
        if not string:
            return result


print("Полученный список: ", lst := fill_list())

print("Произведение пар чисел списка: ", list(lst[i] * lst[-i-1] for i in range((len(lst) + 1) // 2)))

