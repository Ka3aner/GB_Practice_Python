# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

N = float(input("Введите число: "))
result = ""

if not N.is_integer():  # Если число не целое, то необходимо ввести точность приближения
    accuracy = int(input("Введите точность приближения (количество дробных знаков): "))
else:
    N = int(N)  # Если число целое, то меняем тип на int для красивого вывода

whole = int(N)  # Целая часть числа
fract = N % 1  # дробная часть числа

while whole:  # Перевод целой части в двоичный код
    result = result + str(whole % 2)
    whole //= 2
result = result[::-1]

if type(N) != int:
    len_whole = len(result)
    result += "."

while fract and len(result) < len_whole + accuracy + 1:  # Перевод дробной части в двоичный код
    fract *= 2
    result += str(int(fract))
    fract %= 1

print(f"Число {N} в двоичном представлении: {result}")
