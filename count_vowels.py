"""**Описание:**
Напишите функцию **`count_vowels(string)`**, которая подсчитывает количество гласных букв в строке
(гласные: **`a, e, i, o, u`**).
**Требования:**
- Функция должна принимать один аргумент: строку **`string`**.
- Используйте цикл **`for`** для перебора символов строки.
- Гласные буквы могут быть как в нижнем, так и в верхнем регистре.
- Верните результат из функции.
- Выведите результат с помощью функции **`print()`**.
**Пример:**
Если вызвать функцию **`count_vowels("Hello World")`**, то она должна вернуть:
**`3`**
**Вывод результата:**
Количество гласных в строке "Hello World": 3"""
def count_vowels(string):
    string_letters = list(string)
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in string_letters:
        if letter in vowels:
            count += 1
    return count

string = "Hello World"
count_vowels(string)
print(f'Количество гласных в строке "{string}": {count_vowels(string)}')