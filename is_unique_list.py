"""
**Описание:**
Напишите функцию **`is_unique_list(lst)`**, которая принимает список и возвращает **`True`**, если все элементы
списка уникальны, и **`False`**, если есть повторения.
**Требования:**
- Функция должна принимать один аргумент: список **`lst`**.
- Верните **`True`**, если все элементы уникальны, иначе — **`False`**.
**Пример:**
print(is_unique_list([1, 2, 3, 4]))  # True
print(is_unique_list([1, 2, 2, 3]))  # False
"""
def is_unique_list(lst):
    if len(lst) == len(set(lst)):
        return True
    else:
        return False

print(is_unique_list([1, 2, 3, 4]))  # True
print(is_unique_list([1, 2, 2, 3]))  # False
