""" Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
ввёл число 3. Считаем 3 + 33 + 333 = 369. """

user_input = int(input('Введите число до 999: '))

result = user_input

if result < 10:
    result_second = user_input * 11
    result_third = user_input * 111
    total = result + result_second + result_third
    print(f'{result} + {result_second} + {result_third} = {total}')
elif result < 100:
    result_second = user_input * 101
    result_third = user_input * 10101
    total = result + result_second + result_third
    print(f'{result} + {result_second} + {result_third} = {total}')
else:
    result_second = user_input * 1001
    result_third = user_input * 1001001
    total = result + result_second + result_third
    print(f'{result} + {result_second} + {result_third} = {total}')