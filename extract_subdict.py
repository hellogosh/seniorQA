"""
Напишите функцию **`extract_subdict(my_dict, keys)`**, которая принимает словарь и список ключей. Функция должна
вернуть новый словарь, включающий только те пары, ключи которых содержатся в списке.
**Требования:**
- Функция должна принимать два аргумента: словарь **`my_dict`** и список ключей **`keys`**.
- Верните новый словарь.
**Пример:**
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
print(extract_subdict(my_dict, keys))  # {"a": 1, "c": 3}
"""
def extract_subdict(my_dict, keys):
    final_dict = {}
    for key in keys:
        if key in my_dict:
            final_dict[key] = my_dict[key]
    return final_dict

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
print(extract_subdict(my_dict, keys))  # {"a": 1, "c": 3}