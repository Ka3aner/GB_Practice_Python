# Функция заполнения листа c проверкой на число
def fill_list_numbers():
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