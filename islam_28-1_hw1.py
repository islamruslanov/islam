
manday = int(input(f"введите  сумму расходов  в среду:"))
tuesday = int(input(F'введите сумму расходов во вторник:'))
wednesday = int(input(f'введите сумму расходов в среда:'))
thursday = int(input(f'введите сумму расходов в четверг:'))
friday = int(input(f'введите сууму расходов в пятницу:'))
saturday = int(input(f'введите сумму расходов в субота:'))
sundays = int(input(f'введите  сумму расходов в вокресение:'))
a = int(manday+tuesday+wednesday+thursday+friday+sundays)
week = 7
b = round(a / week,1)

print(f'средний расход в день:{b}')
print(f'обшая сумма расходов:{a} ')