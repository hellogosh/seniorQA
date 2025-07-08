tester_bugs = {'Анна': 3, 'Иван': 5, 'Дмитрий': 7}
name_tester = input("Введите имя тестировщика: ")

print(f"Исходные данные: {tester_bugs}")

if name_tester in tester_bugs:
    tester_bugs[name_tester] += 1
else:
    tester_bugs[name_tester] = 1

print(f"Обновленные данные: {tester_bugs}")