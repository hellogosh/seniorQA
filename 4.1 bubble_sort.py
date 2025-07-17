numbers = input('Введите числа через запятую: ')
numbers = [int(num.strip()) for num in numbers.split(',')]
def bubble_sort(numbers):
    n = int(len(numbers))
    for i in range(0, (n - 1)):
        for j in range(0, n - i -1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[i]
    return numbers

sorted_numbers = bubble_sort(numbers)
print(f'Отсортированный список: {sorted_numbers}')