# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

print('Input a number forom 1 to 7: ', end='')
n = int(input())
def DaysOfWeek(n):
    if n >= 1 and n <= 7:
        if n == 6 or n == 7:
            print('{n} -> weekend')
        else:
            print('{n} -> is not a weekend')
    else: print('The number is out of range')
DaysOfWeek(n)

# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('Input X coordinate: ')
x = int(input())
print('Input Y coordinate: ')
y = int(input())
def Coordinate(x, y):
    if x != 0 and y != 0:
        if  x > 0 and y > 0:
            print('First quarter')
        elif x < 0 and y > 0:
            print('Second quarter')
        elif x < 0 and y < 0:
            print('Third quarter')
        elif x > 0 and y < 0:
            print('Fourth quarter')
    else: print('X and Y coordinate must not be 0')
Coordinate(x, y)

# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('Type number of quarter: ', end='')
quarter = int(input())
def QuaterNumber(quarter):
    if quarter == 1:
        print('X coordinate is > 0 and Y coordinate is > 0')
    elif quarter == 2:
        print('X coordinate is < 0 and Y coordinate is > 0')
    elif quarter == 3:
        print('X coordinate is < 0 and Y coordinate is < 0')
    elif quarter == 4:
        print('X coordinate is > 0 and Y coordinate is < 0')
    else: print('the number of quarter is not correct!')
QuaterNumber(quarter)

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
from math import sqrt

print('Input X coordinate of A: ', end='')
x1 = float(input())
print('Input Y coordinate of A: ', end='')
y1 = float(input())
print('Input X coordinate of B: ', end='')
x2 = float(input())
print('Input Y coordinate of B: ', end='')
y2 = float(input())
def DistanceAB(x1, y1, x2, y2):
    ab = math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))
    print('Distance between A and B is: ', ab)
DistanceAB(x1, y1, x2, y2)

# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            print(f'¬(X ⋁ Y ⋁ Z) = ¬({x} ⋁ {y} ⋁ {z}) = {not(x or y or z)}')
            print(f'¬X ⋀ ¬Y ⋀ ¬Z = ¬{x} ⋀ ¬{y} ⋀ ¬{z} = {not x and not y and not z}')