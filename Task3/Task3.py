#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка.
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

n = int(input('Введити координаты точки х: '))
m = int(input('Введити координаты точки y: '))
if n > 0 and m > 0:
        print ('Точка находится в 1 четверти плоскости')
elif n < 0 and m > 0:
        print ('Точка находится во 2 четверти плоскости')
elif n < 0 and m < 0:
        print ('Точка находится в 3 четверти плоскости')
elif n > 0 and m < 0:
        print ('Точка находится в 4 четверти плоскости')
else:
        print ('Вы ввели некорректные координаты точек')