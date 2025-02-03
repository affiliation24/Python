def my_imt(height, weight):
    com = 'Ваш ИМТ: '
    imt = 0

    if height != 0:
        height /= 100
        imt = round(weight / pow(height, 2))
    else:
        print('Ошибка')
        return

    print(f'{com}{imt}')

height = int(input("Введите рост: "))
weight = int(input("Введите вес: "))
my_imt(height, weight)
