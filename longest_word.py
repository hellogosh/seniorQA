"""
**Описание:**
Напишите функцию **`longest_word(s)`**, которая возвращает самое длинное слово в строке.
**Требования:**
- Функция должна принимать один аргумент: строку **`s`**.
- Верните самое длинное слово.
**Пример:**
longest_word("In the middle of a vast desert, an extraordinary adventure awaits")  # "extraordinary”
"""
def longest_word(s):
    words = s.split()
    longest = words[0]
    for i in range(1, len(words)):
        current_word = longest
        next_word = words[i]
        if len(next_word) > len(current_word):
            longest = next_word
    return longest

print(longest_word("In the middle of a vast desert, an extraordinary adventure awaits"))