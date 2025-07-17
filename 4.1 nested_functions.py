def calculator(a, b, operation):
    def result_operation():
        if operation == '+':
            return (a + b)
        elif operation == '-':
            return (a - b)
        elif operation == '*':
            return (a * b)
        elif operation == '/':
            return (a / b)
    print(f'Результат: {result_operation()}')

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
operation = input('Выберите операцию (+, -, *, /): ')

calculator(a, b, operation)