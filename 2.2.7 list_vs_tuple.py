num_list = [4, 7, 9, 2, 5]
num_tuple = (4, 7, 9, 2, 5)

print(f'Исходный список: {num_list} ')
print(f'Исходный кортеж: {num_tuple}')

num_list[1] = 10
print(f'Измененный список: {num_list}')
print('Ошибка: Кортеж нельзя изменить!')

num_list.append(6)
print(f'Добавленный элемент в список: {num_list}')
print("Ошибка: В кортеж нельзя добавить элемент!")
