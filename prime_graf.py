import pandas as pd
import matplotlib.pyplot as plt

# Функция для проверки, является ли число простым
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Функция для поиска простых чисел и подсчёта их количества
def find_primes_up_to_n(n):
    primes = []
    counts = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
        counts.append(len(primes))  # Сохраняем текущее количество простых чисел
    return primes, counts

# Ввод диапазона
n = int(input("Введите диапазон (n): "))

# Поиск простых чисел и подсчёт их количества
primes, counts = find_primes_up_to_n(n)

# Создаём DataFrame для хранения данных
data = pd.DataFrame({
    'Число': range(2, n + 1),  # Ось X: числа от 2 до n
    'Количество простых чисел': counts  # Ось Y: количество простых чисел
})

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(data['Число'], data['Количество простых чисел'], label='Количество простых чисел', color='blue')
plt.title('Количество простых чисел в диапазоне от 2 до {}'.format(n))
plt.xlabel('Число')
plt.ylabel('Количество простых чисел')
plt.grid(True)
plt.legend()
plt.show()