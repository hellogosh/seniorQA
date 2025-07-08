error_log = input("Введите строку лога: ")

processed_str = error_log.strip()
replaced_str = processed_str.replace('Ошибка', 'Ошибка критическая')

print(f'Разбитый текст:  {replaced_str.split()}')
print(f'Обработанная строка: {processed_str}')