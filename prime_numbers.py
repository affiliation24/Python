from math import *

# получение простых чисел

n = int(input("Введите диапазон:- "))
p = [2, 3]
count = 2
a = 5

while count < n:
    b = 0
    for i in range(2, a):
        if i <= sqrt(a):  # Используем sqrt из модуля math
            if a % i == 0:
                print("Не простое", a)
                b = 1
            else:
                pass
    if b != 1:
        print("Простое", a)
        p = p + [a]
        count = count + 1
    a = a + 2

print(p)
print('Количество простых чисел: ', count)