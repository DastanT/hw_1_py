""" Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк. """


user_input_sec = int(input())
hours = int(user_input_sec / 3600)
minutes_ost = int(user_input_sec % 3600)
minutes = int(minutes_ost / 60)
seconds = int(minutes_ost % 60)
if minutes > 10: 
    if seconds > 10:
        print(f'{hours}:{minutes}:{seconds}')
elif minutes > 10:
    if seconds < 10:
        print(f'{hours}:{minutes}:0{seconds}')
elif minutes < 10:
    if seconds > 10:
        print(f'{hours}:0{minutes}:{seconds}')
    else:
        print(f'{hours}:0{minutes}:0{seconds}')