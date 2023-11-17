numbers_tuple = (5, 2, -2, 7, -8, -9, 1)

sign_changes = 0
previous_sign = 0

for num in numbers_tuple:
    current_sign = 1 if num >= 0 else -1

    if previous_sign != 0 and current_sign != previous_sign:
        sign_changes += 1

    previous_sign = current_sign

print(f"Число изменений знака: {sign_changes}")
