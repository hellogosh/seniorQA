n = int(input("Введите число: "))

print("Числа:", end = " ")
for i in range(n):
    print(i + 1, end = " ")
print()

total = 0
for i in range(n+1):
    total += i
print(f"Сумма чисел: {total}")


