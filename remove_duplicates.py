"""
**Описание:**
Напишите функцию **`remove_duplicates(s)`**, которая принимает строку и возвращает новую строку, из которой удалены все
повторяющиеся символы, оставляя только первое вхождение каждого символа.
**Требования:**
- Функция должна принимать один аргумент: строку **`s`**.
- Верните строку без повторяющихся символов.
**Пример:**
remove_duplicates("programming")  # "progamin”
"""
def remove_duplicates(s):
    seen = set()
    result = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return ''.join(result)

print(remove_duplicates("programming"))
