def find_min(a, b):
    return min(a, b)


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
num4 = int(input("Введите четвертое число: "))

min_of_four = find_min(find_min(num1, num2), find_min(num3, num4))
print(f"Минимальное из четырех чисел: {min_of_four}")
