def closest_mod_5(x):
    return x + (5 - x % 5) % 5


input_number = int(input("Введите целое число x: "))
result = closest_mod_5(input_number)
print(f"Ближайшее число, кратное 5 и большее или равное {input_number}: {result}")
