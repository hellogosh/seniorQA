monday_num = int(input("Какое количество тест-кейсов, выполнено в понедельник? :"))
tuesday_num = int(input("Какое количество тест-кейсов, выполнено в вторник? :"))
wednesday_num = int(input("Какое количество тест-кейсов, выполнено в среду? :"))
thursday_num = int(input("Какое количество тест-кейсов, выполнено в четверг? :"))
friday_num = int(input("Какое количество тест-кейсов, выполнено в пятницу? :"))
saturday_num = int(input("Какое количество тест-кейсов, выполнено в субботу? :"))
sunday_num = int(input("Какое количество тест-кейсов, выполнено в воскресение? :"))

total_number_per_week = (monday_num + tuesday_num + wednesday_num + thursday_num + friday_num + saturday_num + sunday_num)

average_number_per_day = (total_number_per_week / 7)

print(f'Общее количество : {total_number_per_week} тест-кейсов за неделю')
print(f'Среднее количество {average_number_per_day} тест-кейсов в неделю')

if average_number_per_day > 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")
