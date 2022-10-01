# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов
# списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Функция заполнения листа c проверкой на число
def fill_list():
    result = []
    while True:
        str = input("Введите элемент листа (Нажмите 'Enter', чтобы закончить): ")
        if str.isdigit():
            result.append(int(str))
        elif str.replace(".", "", 1).isdigit():
            result.append(float(str))
        elif str:
            print("Введено не число. Строка не попала в лист")
        if not str:
            return result


print("Полученный список: ", lst := fill_list())

print("Сумма элементов списка, стоящих на нечётной позиции равна: ",
      sum(lst[i] for i in range(len(lst)) if i % 2))
