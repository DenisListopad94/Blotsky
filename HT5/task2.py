def generate_numbers():
    numbers_list = [num for num in range(100, 1000) if num % 5 == 0 and num % 3 == 0]
    return numbers_list


result = generate_numbers()
print(result)
