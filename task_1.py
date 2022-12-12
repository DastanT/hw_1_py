"""
Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

"""
name = input('Enter your login: ')
password = input('Enter your password: ')

# функция проверки на корректность (в случае, если пользователь введет буквенные значения)
def is_age(userInput):
    while True:
        x = input(userInput)
        try:        
            return int(x)
        except ValueError:
            print('Error. Please enter your age!')

age = is_age('Enter your age: ')

print('\nLogin: ', name)
print('Password: ', password)
print('Your age: ', age)