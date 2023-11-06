a = int(input("Введите длину прямоугольника (в см): "))
b = int(input("Введите ширину прямоугольника (в см): "))

square_side = 30
squares = (a // square_side) * (b // square_side)

# Вывод результата
print(f"Можно отрезать {squares} квадратов.")
