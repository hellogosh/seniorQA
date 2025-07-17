def check_triangle(a, b, c):
    try :
        if a >= (b + c) or b >= (a + c) or c >= (a + b):
            raise ValueError('Каждая сторона должна быть меньше суммы двух других.')
        elif a == b == c:
            print("Результат: Треугольник равносторонний")
        elif a == b or b == c or a == c:
            print("Результат: Треугольник равнобедренный")
        else:
            print("Результат: Треугольник разносторонний")
    except ValueError as error:
        print(error)

a = int(input('Введите длину первой стороны: '))
b = int(input('Введите длину второй стороны: '))
c = int(input('Введите длину третьей стороны: '))

check_triangle(a, b, c)