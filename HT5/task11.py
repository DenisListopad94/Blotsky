original_list = [5, 2, 0, -2, -7, 1, 8, 0, -1]

positive_numbers = [num for num in original_list if num > 0]
negative_and_zeros = [num for num in original_list if num <= 0]

result_list = positive_numbers + negative_and_zeros

print(result_list)
