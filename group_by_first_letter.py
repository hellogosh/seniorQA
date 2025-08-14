"""
Напишите функцию **`group_by_first_letter(strings)`**, которая принимает список строк и группирует их в словарь,
где ключами являются первые символы строк, а значением — список строк, начинающихся с этого символа.
**Требования:**
- Функция должна принимать один аргумент: список строк **`strings`**.
- Верните словарь с группировкой.
**Пример:**
strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))
# {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}
"""
def group_by_first_letter(strings):
    final_dict = {}
    for i in strings:
        key = i[0]
        if key not in final_dict:
            final_dict[key] = []
        final_dict[key].append(i)
    return final_dict

strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))
