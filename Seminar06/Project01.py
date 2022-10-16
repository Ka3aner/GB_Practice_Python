# 1 – Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

def math_action(x, y, symbol):
    match symbol:
        case "-":
            return x - y
        case "+":
            return x + y
        case "*":
            return x * y
        case "/":
            return x / y


def parse_expression(exp: str):
    # Проверка выхода из рекурсии
    try:
        return float(exp)
    except ValueError:
        pass

    # Цикл будет идти до тех пор, пока мы не подсчитаем все скобки ВКЛЮЧАЯ вложенные
    while "(" in exp:
        start_position = 0
        for i in range(len(exp)):
            if exp[i] == "(":
                start_position = i
            if exp[i] == ")":
                end_position = i
                slice = exp[start_position:end_position + 1]
                return parse_expression(exp.replace(slice, str(parse_expression(slice[1:-1]))))

    symbols = "+-*/"
    for symbol in symbols:
        left_value, right_value = exp.partition(symbol)[0], exp.partition(symbol)[2]
        if left_value == exp:
            continue
        return math_action(parse_expression(left_value), parse_expression(right_value), symbol)


value = "(5 + 4 * ((2 + 3) * 7 + 6 * (8 + 9)) - 9)"
value = "".join(value.split())
print(f"Исходное выражение: {value}")
result = parse_expression(value)
print(f"Решение арифметического выражения: {int(result) if result % 1 == 0 else result }")
print(f"Проверка через eval: {eval(value)}")