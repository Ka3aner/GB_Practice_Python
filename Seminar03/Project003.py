# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

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

Min = lst[0]
Max = lst[0]

for number in lst:
    if not number % 1:
        continue
    if number % 1 > Max % 1:
        Max = number
    elif number % 1 < Min % 1:
        Min = number

print(f"Разность между максимальным ({Max}) и минимальным ({Min}) значением дробной части элементов списка: "
      f"{Max % 1 - Min % 1}")
