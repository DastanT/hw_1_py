""" Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции """

user_input = int(input('Введите число больше 0: '))

max_number = 0

while user_input != 0:
    # с конца берем цифру
    current_number = user_input % 10
    if max_number < current_number:
        max_number = current_number
    # уменьшам введенное число на одну цифру с конца
    user_input = user_input // 10

print(f'Максимальное число: {max_number}')