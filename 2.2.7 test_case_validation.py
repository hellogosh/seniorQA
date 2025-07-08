while True:
    test_case_quantity = input("Введите количество тест-кейсов: ")

    try:
        n = int(test_case_quantity)
        if n > 10:
            print('Отличная работа!')
            break
        elif 10 >= n > 0:
            print('Попробуйте улучшить результат.')
            break
        elif n <= 0:
            print("Некорректный ввод. Введите положительное число.")
    except ValueError:
        print("Некорректный ввод. Введите положительное число.")
