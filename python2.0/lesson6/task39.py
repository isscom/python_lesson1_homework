# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива

# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

# Вывод
# 3 3 2 12

N = int(input('N - кол-во элементов в I массиве:\n'))
array_N = [int(i) for i in input('Введите элементы массива через пробел:\n').split()][:N] # ровно то кол-во, кот. скажет пользователь
# array_N = [int(input(f'{i+1}/{N} элемент: ')) for i in range(N)] # ввод каждого элемента с новой строки

M = int(input('M - кол-во элементов в II массиве:\n'))
array_M = [int(i) for i in input('Введите элементы массива через пробел:\n').split()][:M]
# array_M = [int(input(f'{i+1}/{M} элемент: ')) for i in range(M)]

print('Ввод:', '\n', N, '\n', *array_N, '\n', M, '\n', *array_M)

# array_result = []

# for i in array_N:
#     if i not in array_M:
#         array_result.append(i)

# array_result = [i for i in array_N if i not in array_M] # с помощью генератора списков выводим аналогичное решение
# print('Вывод:', '\n', *array_result)

print('Вывод:', '\n', *[i for i in array_N if i not in array_M]) # не создавая список array_result сразу добавляем генератор списков в вывод print




# ТАКЖЕ МОЖНО РЕШИТЬ ЗАДАЧУ ЧЕРЕЗ МНОЖЕСТВА (вычитать одно из другого)

X = N # берем аналогичные значения из 1-го решения
# array_X = set([int(i) for i in input('Введите элементы массива через пробел:\n').split()][:X])
array_X = set(array_N)

Y = M # берем аналогичные значения из 1-го решения
# array_Y = set([int(i) for i in input('Введите элементы массива через пробел:\n').split()][:Y])
array_Y = set(array_M)

print('Вывод (результат вычитания множеств):', '\n', *(array_X - array_Y))
# учитывая повторяющиеся элементы в первом множестве - это решение (с set()) не подходит для решения,
# но имеет место быть в других задачах (просто, чтобы помнить о функциях работы со множествами)