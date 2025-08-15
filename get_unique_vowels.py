"""
Создайте функцию **`get_unique_vowels(s)`**, которая принимает строку и возвращает набор уникальных гласных,
содержащихся в строке (игнорируя регистр).
**Требования:**
- Функция должна принимать один аргумент: строку **`s`**.
- Гласные буквы: **`a, e, i, o, u`**.
- Игнорируйте регистр символов.
- Верните множество уникальных гласных.
**Пример:**
print(get_unique_vowels("Hello World"))  # {'e', 'o'}
"""
def get_unique_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_s = []
    for i in s:
        if i in vowels:
            vowels_in_s.append(i)
    return set(vowels_in_s)

print(get_unique_vowels("Hello World"))  # {'e', 'o'}
