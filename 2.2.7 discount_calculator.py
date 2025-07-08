purchase_amount = float(input("Введите сумму покупки: "))
discount_percentage = float(input("Введите процент скидки: "))

savings_amount = purchase_amount * (discount_percentage/100)
paid_amount = purchase_amount - savings_amount

print(f'Вы экономите: {purchase_amount * (discount_percentage/100)}')
print(f'Сумма к оплате (округлено): {round(paid_amount)}')
