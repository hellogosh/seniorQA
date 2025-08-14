"""
**Описание:**
Напишите функцию **`is_palindrome(s)`**, которая проверяет, является ли строка палиндромом (читается одинаково слева
направо и справа налево). Игнорируйте пробелы, знаки препинания и регистр.
**Требования:**
- Функция должна принимать один аргумент: строку **`s`**.
- Верните **`True`**, если строка является палиндромом, иначе — **`False`**.
**Пример:**
is_palindrome("A man, a plan, a canal: Panama")  # True
is_palindrome("racecar")                         # True
is_palindrome("hello")                           # False
"""
def is_palindrome(s):
    s_new = s.replace(" ", "").lower().replace(",", "").replace(".","").replace(":","")
    return s_new == s_new[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))