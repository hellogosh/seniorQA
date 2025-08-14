"""
Напишите функцию **`remove_duplicates(lst)`**, которая удаляет все повторяющиеся элементы из списка, оставляя только
 уникальные значения.
**Требования:**
- Функция должна принимать один аргумент: список **`lst`**.
- Верните список без повторяющихся элементов.
**Пример:**
print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # [1, 2, 3, 4]
"""
def remove_duplicates(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4]))
