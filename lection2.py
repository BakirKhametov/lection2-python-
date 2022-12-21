# Работа с файлами:
# Связать файловую переменную с файлом, определив модификатор работы
# а - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для записи данных

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # а, r , w  - в зависимости от требования добавления, записи или чтения данных
# data.writelines(colors)
# data.write('LINE 12\n')
# data.write('LINE 32\n')
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('LINE 1111\n')
#     data.write('LINE 2222\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

    # import <название фунции без кавычек> as <короткое название>
    # Например:
# # import hello as h////
# print(h.f(1))/////
    # Функция из первой лекции: название файла лекции было "hello"  
    # def f(x):
    #     if x == 1:
    #         return 'Целое'
    #     elif x == 2.3:
    #         return 23
    #     else:
    #         return   

# Функции:
# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!', 5)) # Результат: !!!!!
# print(new_string('!', 3)) # Результат: !!!
# print(new_string('!')) # Результат: Выдаст ошибку, так как первое значение умножается на второе:
#                                   ! * 5 = !!!!!, так как нет второго значения то будет ошибка

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5)) # Результат: !!!!!
# print(new_string('!', 3)) # Результат: !!!
# print(new_string(4)) # Результат: 12

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w'))    # Результат aswd
# print(concatenatio('a', '1'))  # Результат a1

# def concatenatio(*params):
#     res: int = 0
#     for item in params:
#         res += item
#     return res
# print(concatenatio(1, 2, 3, 4))    # Результат 10: 1+2+3+4

#Функция рекурсии
# def fibanacci(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fibanacci(n-1) + fibanacci(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fibanacci(e))
# print(list)  # Результат [1, 1, 2, 3, 5, 8, 13, 21, 34]  Последовательность Фибаначчи. 

# Кортежи
# a = (3, 4)
# print(a) # Результат (3, 4)
# print(a[0]) #Результат 3. Вывод по индексу элемента

# a = (3, 1, 41, 4)
# print(a) # Результат (3, 4)
# print(a[-1]) #Результат 4. Вывод по индексу элемента работает и в обратную строну при помощи отрицательного индекса
# print(a[-2]) #Результат 41

# a[0] = 12 # Присвоение к конкретному индексу элемента: а с нулевым индексом будет иметь значение 12

# Словари
# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary['left'])  # ←
# for k in dictionary.keys():
#     print(k)    # Вывод всех ключей         #up
#                                             # left
#                                             # down
#                                             # right
# for k in dictionary.values():
#     print(k) # Вывод значений ключей :
#                                             # ↑
#                                             # ←
#                                             # ↓
#                                             # →

# Множества
# Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 1

# Неизменяемое множество
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# Списки. Особенности
# list1 = [1,2,3,4,5]  # pop - удаление последнего элемента списка 
# print(list1)  # [1, 2, 3, 4, 5]
# print(list1.pop()) # 5
# print(list1) # [1, 2, 3, 4]
# print(list1.pop()) # 4

# list1 = [1,2,3,4,5]  # pop(2) - удаление конкретного элемента списка с индексом 2
# print(list1.pop(2)) # 3
# print(list1)  # [1, 2, 3, 4, 5]

# list1 = [1,2,3,4,5]  # insert(2, 11) - вставка конкретного элемента списка с индексом 2 и числом 11
# print(list1.insert(2, 11)) # None
# print(list1) # [1, 2, 11, 3, 4, 5]

# list1 = [1,2,3,4,5]  # append(11) - вставка  элемента в конец списка с последним индексом  и числом 11
# print(list1.append(11)) # None
# print(list1) # [1, 2, 3, 4, 5, 11]
