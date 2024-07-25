from math import ceil
square = float(input("Введите значение стороны квадрата "))
if (square > 0):
    print (ceil(square * square))
else:
    print("Cторона кравадрата не может быть отрицательной")
