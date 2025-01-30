import math

def is_valid(a, b, c):
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

def triangle_type(a, b, c):
    if a**2 + b**2 > c**2 and b**2 + c**2 > a**2 and c**2 + a**2 > b**2:
        return "Остроутольный треугольник"
    elif a**2 + b**2 < c**2 or b**2 + c**2 < a**2 or c**2 + a**2 < b**2:
        return "Тупоугольный треугольник"
    else:
        return "Прямоугольный треугольник"

def triangle_area(a, b, c): 
    s = (a + b + c) / 2 
    return f"Area - {math.sqrt(s * (s - a) * (s - b) * (s - c))}" 

def main():
    try:
        a = float(input("Введите длину первой стороны треугольника: "))
        b = float(input("Введите длину второй стороны треугольника: "))
        c = float(input("Введите длину третьей стороны треугольника: "))

        if not is_valid(a, b, c):
            print("err:The values entered cannot be sides of a triangle.")
            return

        t_type = triangle_type(a, b, c)
        area = triangle_area(a, b, c)

        print(f"Вид треугольника: {t_type}")
        print(f"Площадь треугольника: {area:.2f}")

    except ValueError:
        print("err: Please enter valid numeric values.")

if __name__ == "__main__":
    main()
