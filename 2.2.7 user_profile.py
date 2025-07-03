name = input("Кто ты, воин?:")
profession = input("Какова твоя профессия?:")
tool = input("Назови свои любимый инструмент:")

if not name:
    print("Имя не указано. Попробуй снова!")
else:
    print(f"Приветствую, {name}!")


if not profession:
    print("Профессия не указана. Попробуй снова!")
else:
    print(f"Понял! Твоя профессия - {profession}.")


if not tool:
    print("Инструмент не указан. Попроуй еще!")
else:
    print(f"Ваш любимый инструмент: {tool}. Отличный выбор!")