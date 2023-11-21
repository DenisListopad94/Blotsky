list1 = [4, 1, 6, 9]
list2 = [8, 1, 2, 4, 9, 5, 7, 6]

min_not_in_list = 0

for num in list1:
    if num != list2:
        if min_not_in_list != 0 | num < min_not_in_list:
            min_not_in_list = num
            
if min_not_in_list != 0:
    print(min_not_in_list)
else:
    print("not exist")
    
