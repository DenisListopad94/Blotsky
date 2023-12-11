original_list = [5, 2, 7, 3, 8, 2, 4, 1, 6, 5]

element_count = {}

duplicated_list = []
for num in original_list:
    if num not in element_count:
        element_count[num] = 1
        duplicated_list.extend([num, num])
    else:
        duplicated_list.append(num)

print(duplicated_list)
