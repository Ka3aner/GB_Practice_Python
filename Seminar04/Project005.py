# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import sympy


def FileWorks(file_name, method,
              output=0):  # Функция принимает имя файла, метод открытия и опционально переменную вывода
    if method == "r":  # Если мы хотим считать файл
        with open(file_name, method, encoding="utf-8") as file:
            return file.read()  # Возвращаем значения
    elif method == "w":  # Если мы хотим записать файл
        if output:  # Проверяем, внесли ли значения в функцию
            with open(file_name, method, encoding="utf-8") as file:
                file.write(str(output.as_expr()).replace('**', '^') + " = 0")


x = sympy.Symbol('x')

# Объъявляем переменные, используя функцию, убирая приравнивание к 0 и превращая строку в понятный для sympy тип данных
z1 = sympy.polys.polytools.poly_from_expr(FileWorks("input1.txt", "r").replace(" = 0", ""))[0]
z2 = sympy.polys.polytools.poly_from_expr(FileWorks("input2.txt", "r").replace(" = 0", ""))[0]

# Запускаем функцию вывода, передавая сумму многочленов
FileWorks("output_prog_4.txt", "w", z1 + z2)
