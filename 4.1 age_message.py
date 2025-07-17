def age_message(age):
    if age < 18:
        print("Вы еще молоды, учеба — ваш путь!")
    elif age > 65:
        print("Пора наслаждаться заслуженным отдыхом!")
    else:
        print("Отличный возраст для карьерного роста!")

age_input = int(input('Введите год вашего рождения: '))
age = 2025 - age_input

print(f'Ваш возраст: {age}')
age_message(age)

