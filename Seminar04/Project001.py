# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

n = float(input("Введите число: "))
accuracy = input("Введите точность округления: ")

print(f"Округленное число {n} с указанной точностью {accuracy} равно {round(n, accuracy.count('0'))}")