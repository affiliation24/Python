def check_ever_odd(number):
    if number % 2 == 0:
        return f'Число {number} чётное.'
    else:
        return f'Число {number} нечётное.'

def compare_numbers(num1, num2):
    if num1 > num2:
        return f'\n {num1} больше {num2}'
    elif num1 < num2:
        return f'\n {num1} меньше {num2}'
    else:
        return f'{num1} и {num2} равны'

def calculator():
    print('Добро пожаловать в калькулятор')

    while True:
        # print("\n Выберите операцию:")
        print("\n 1. Проверить чётность числа")
        print("\n 2. Сравнить два числа")
        print("\n 3. Выйти")

        choice = input("\nВыберите операцию: ")

        if choice == '1':
            number = input("\nВведите число: ")
            print(check_ever_odd(number))

        elif choice == '2':
            num1 = float(input('\n Введи первое число: '))
            num2 = float(input('\n Введи второе число: '))
            print(compare_numbers(num1, num2))

        elif choice == '3':
            print('Выход из калькулятора')
            break

        else:
            print('НЕВЕРНЫЙ ВЫБОР')

calculator()