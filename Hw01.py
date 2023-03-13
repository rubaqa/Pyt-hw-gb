# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# x = int(input('Введите номер дня недели - '))
# print(x)
# if ( x == 6 or x == 7):
#     print('Да')
# else:
#     print('Нет')
#
#
#2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# x = float(input('Введите координату х - '))
# y = float(input('Введите координату y - '))
# if x > 0 and y > 0:
#     print('Точка находится в 1 четверти')
# elif x < 0 and y > 0:
#     print('Точка находится в 2 четверти')
# elif x < 0 and y < 0:
#     print('Точка находится в 3 четверти')
# elif x > 0 and y < 0:
#     print('Точка находится в 4 четверти')
# else:
#     print('Вы ввели что-то не то')
#
#
#3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
#
# n = int(input('Введите номер четверти - '))
# if n == 1:
#     print('Возможные координаты - x > 0 и y > 0')
# elif n == 2:
#     print('Возможные координаты - x < 0 и y > 0')
# elif n == 3:
#     print('Возможные координаты - x < 0 и y < 0')
# elif n == 4:
#     print('Возможные координаты - x > 0 и y < 0')
# else:
#     print('Вы ввели что-то не то')
#
#
#4. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

descrip = ['X1','Y1','X2','Y2']
coord_list = []
for i in range(len(descrip)):
    coord_list.append(float(input(f'Введите координату {descrip[i]}: ')))
distance = ((coord_list[2] - coord_list[0])**2 + (coord_list[3] - coord_list[1])**2)**0.5
print(f'Расстояние между точками с координатами ({coord_list[0]}, {coord_list[1]}) и ({coord_list[2]}, {coord_list[3]}) = {round(distance,2)}')