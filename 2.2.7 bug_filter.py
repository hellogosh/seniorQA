bug_list = ["Ошибка 1 – High", "Ошибка 2 – Medium", "Ошибка 3 – Low", "Ошибка 4 – High", "Ошибка 5 – Medium", "Ошибка 6 – High", "Ошибка 7 – Low"]

priority = input("Введите приоритет для поиска (High, Medium, Low): ")

filtered_bugs = [i for i in bug_list if priority in i]

if filtered_bugs:
    print("Найденные баги:")
    for i in filtered_bugs:
        print("-", i)
else:
    print("Баги с таким приоритетом не найдены.")