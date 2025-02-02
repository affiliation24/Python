import sys
import os

print('\n',os.getcwd())  #текущий каталог программы

print('\n Аргументы командной строки:')
for i in sys.argv:
    print(i)
print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')