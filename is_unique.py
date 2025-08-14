"""
Напишите функцию **`is_unique(s)`**, которая проверяет, содержит ли заданная строка все уникальные символы
(без повторов).
**Требования:**
- Функция должна принимать один аргумент: строку **`s`**.
- Верните **`True`**, если все символы уникальны, иначе — **`False`**.
**Пример:**
is_unique("abcdef")  # True
is_unique("hello")  # False
"""
def is_unique(s):
    return len(s) == len(set(s))

print(is_unique("abcdef"))
print(is_unique("hello"))
