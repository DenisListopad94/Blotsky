numbers = [5, 2, 4, 5, 1, 2]

count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

for key, value in count_dict.items():
    print(f"{key} --> {value}")
