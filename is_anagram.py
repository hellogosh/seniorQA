"""
**Описание:**
Напишите функцию **`is_anagram(s1, s2)`**, которая проверяет, являются ли две строки анаграммами (перестановками друг
друга).
**Требования:**
- Функция должна принимать два аргумента: строки **`s1`** и **`s2`**.
- Игнорируйте регистр символов.
- Верните **`True`**, если строки являются анаграммами, иначе — **`False`**.
**Пример:**
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
"""
def is_anagram(s1, s2):
    s1_new = s1.lower()
    s2_new = s2.lower()
    return sorted(s1_new) == sorted(s2_new)

print(is_anagram("listen", "netsil"))
print(is_anagram("hello", "world"))