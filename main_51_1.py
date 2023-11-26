# If Else

"""
1. Даны три целых числа.
Найти количество положительных чисел в исходном наборе.
"""

first_number = int(input("Введите первое число: \n"))
second_number = int(input("Введите второе число \n"))
third_number = int(input("Введите третье число \n"))

count = 0

if first_number > 0:
    count += 1
if second_number > 0:
    count += 1
if third_number > 0:
    count += 1
print(count)


"""2. Даны два числа. Вывести большее из них."""

first_number = int(input("Введите первое число: \n"))
second_number = int(input("Введите второе число \n"))

if first_number > second_number:
    print(first_number)
elif first_number < second_number:
    print(second_number)
else:
    print("Числа равны")


"""3. Даны два числа. 
Вывести вначале большее, а затем меньшее из них."""

first_number = int(input("Введите первое число: \n"))
second_number = int(input("Введите второе число \n"))

if first_number > second_number:
    print(first_number, second_number)
elif first_number < second_number:
    print(first_number, second_number)
else:
    print("Числа равны")

"""4. Даны три числа. Найти наименьшее из них."""

first_number = int(input("Введите первое число: \n"))
second_number = int(input("Введите второе число \n"))
third_number = int(input("Введите третье число \n"))

if first_number <= second_number and first_number <= third_number:
    print(first_number)
elif second_number <= first_number and second_number <= third_number:
    print(second_number)
elif third_number <= first_number and third_number <= second_number:
    print(third_number)
else:
    print("Что-то не так с вводом данных")


"""5. Даны координаты точки, не лежащей на координатных осях OX и OY. 
    Определить номер координатной четверти, в которой находится данная точка. 
    Координаты задаются пользователем, например (10, 15)."""


axis_x = int(input("Введите координату на оси Х, "
                   "не лежащей на координатных осях OX и OY: \n "))
axis_y = int(input("Введите координату на оси Y, "
                   "не лежащей на координатных осях OX и OY: \n "))

if axis_x > 0 and axis_y > 0:
    print("Координаты не должны лежать на осях OX и OY. "
          "Введите правильные координаты")
elif axis_x < 0 and axis_y > 0:
    print(f'Введенные точки OX={axis_x} и OY={axis_y} лежат в IV четверти.')
elif axis_x < 0 and axis_y < 0:
    print(f'Введенные точки OX={axis_x} и OY={axis_y} лежат в III четверти.')
elif axis_x > 0 and axis_y < 0:
    print(f'Введенные точки OX={axis_x} и OY={axis_y} лежат в III четверти.')
else:
    print("Введенное значение не должно быть 0.")

