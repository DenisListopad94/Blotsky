numbers_tuple = (6, 2, 7, 8)

for num in numbers_tuple:
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    if divisors_sum == num:
        print(f"{num} - совершенное число")
    if divisors_sum != num:
        print(f"{num} - Несовершенное число")
   