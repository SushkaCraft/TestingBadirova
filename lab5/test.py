import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Бесконечное множество решений"
            else:
                return "Нет решений"
        else:
            x = -c / b
            return f"x = {x:.2f} (линейное уравнение)"
    
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"x1 = {x1:.2f}, x2 = {x2:.2f}"
    elif discriminant == 0:
        x = -b / (2 * a)
        return f"x = {x:.2f} (один корень)"
    else:
        real = -b / (2 * a)
        imaginary = math.sqrt(abs(discriminant)) / (2 * a)
        return f"x1 = {real:.2f} + {imaginary:.2f}i, x2 = {real:.2f} - {imaginary:.2f}i"

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

result = solve_quadratic(a, b, c)
print(result)

# То что ниже необязательно копировать
def test():
    test_cases = [
        (2, -5, 2, "x1 = 2.00, x2 = 0.50"),
        (3, 2, 5, "x1 = -0.33 + 1.25i, x2 = -0.33 - 1.25i"),  # Изменено ожидаемое значение
        (3, -12, 0, "x1 = 4.00, x2 = 0.00"),
        (0, 0, 10, "Нет решений"),
        (0, 0, 0, "Бесконечное множество решений"),
        (0, 5, 17, "x = -3.40 (линейное уравнение)"),
        (9, 0, 0, "x = 0.00 (один корень)")
    ]
    
    for i, (a, b, c, expected) in enumerate(test_cases, 1):
        result = solve_quadratic(a, b, c)
        assert result == expected, f"Тест {i} провален: ожидалось {expected}, получено {result}"
        print(f"Тест {i} пройден\Введено a = {a}, b = {b}, c = {c}\nПолучено - {result}")

test()
