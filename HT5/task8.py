def closest_mod_5(x):
    y = x
    while y % 5 != 0:
        y += 1
    return y

input_number = int(input("Введите целое число x: "))
result = closest_mod_5(input_number)
print(f"Ближайшее число, кратное 5 и большее или равное {input_number}: {result}")
