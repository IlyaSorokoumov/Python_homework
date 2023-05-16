month_number = input("Введите номер месяца: ")
month_lst = [
    ['Январь', 31], #0
    ['Февраль', 28],
    ['Март', 31], #2
    ['Апрель', 30],
    ['Май', 31], #4
    ['Июнь', 30],
    ['Июль', 31], #6
    ['Август', 31],
    ['Сентябрь', 30],
    ['Октябрь', 31],
    ['Ноябрь', 30],
    ['Декабрь', 31],
]
month_num = int(month_number) - 1

if month_num < 0 or month_num > 11:
  print("Такого месяца нет.")
else:
  if month_lst[month_num][1] == 31:
    print(f'Вы выбрали {month_lst[month_num][0]}, в котором {month_lst[month_num][1]} день.')
  else:
    print(f'Вы выбрали {month_lst[month_num][0]}, в котором {month_lst[month_num][1]} дней.')