import math


def is_valid(a, b, c):
    return (a > 0 and b > 0 and c > 0) and (a + b > c) and (a + c > b) and (b + c > a)


def triangle_type(a, b, c):
    if a == b == c:
        return "Равносторонний"
    elif a == b or a == c or b == c:
        return "Равнобедренный"
    else:
        return "Разносторонний"


def angle_type(a, b, c):
    if a ** 2 + b ** 2 > c ** 2 and b ** 2 + c ** 2 > a ** 2 and c ** 2 + a ** 2 > b ** 2:
        return "Остроутольный треугольник"
    elif a ** 2 + b ** 2 < c ** 2 or b ** 2 + c ** 2 < a ** 2 or c ** 2 + a ** 2 < b ** 2:
        return "Тупоугольный треугольник"
    else:
        return "Прямоугольный треугольник"


def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return f"Area - {math.sqrt(s * (s - a) * (s - b) * (s - c))}"


def main():
    try:
        a = float(input("Введите a - "))
        b = float(input("Введите b - "))
        c = float(input("Введите c - "))

        if not is_valid(a, b, c):
            print("err: Not Valid Triangle\n")
            return

        print(triangle_type(a, b, c))

        print(angle_type(a, b, c))

        print(triangle_area(a, b, c))
    except ValueError:
        print("err: Not Valid Value")
        return
    
main()