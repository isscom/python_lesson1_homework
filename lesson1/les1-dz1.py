# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

n = int(input('Введите цифру от 1 до 7, обозначающую день недели: '))
if n == 6 or n == 7:
        print(n," -> да")
elif 0 < n < 6:
        print(n," -> нет")
else:
        print(n," -> число вне пределов 7 дней")