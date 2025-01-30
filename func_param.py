def outputMax(a, b):
    if a > b:
        print(a, 'больше чем', b)
    elif a == b:
        print(a, ' равно', b)
    else:
        print(b, 'больше чем', a)


a = input('Введите значение а: ')
b = input('Введите значение b: ')
outputMax(a, b)
