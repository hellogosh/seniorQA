"""
Напишите функцию **`check_grade(score)`**, которая принимает оценку и возвращает текстовое описание:
- 90–100: "Отлично".
- 75–89: "Хорошо".
- 50–74: "Удовлетворительно".
- Меньше 50: "Неудовлетворительно".
**Требования:**
- Функция должна принимать один аргумент: число **`score`**.
- Используйте конструкцию **`if-elif-else`** для проверки диапазонов.
- Верните результат из функции.
- Выведите результат с помощью функции **`print()`**.
**Пример:**
Если вызвать функцию **`check_grade(85)`**, то она должна вернуть:
**`"Хорошо"`**
**Вывод результата:**
Оценка за 85 баллов: Хорошо.
"""
def check_grade(score):
    if 90 <= score <= 100:
        result = "Отлично"
    elif 75 <= score <= 89:
        result = "Хорошо"
    elif 50 <= score <= 74:
        result = "Удовлетворительно"
    elif 1 <= score <= 49:
        result = "Неудовлетворительно"
    else:
        result = "Число должно быть в диапазоне от 0 до 100"
    return result
score = 100
result = check_grade(score)
print(f' Оценка за {score} баллов: {result}.')