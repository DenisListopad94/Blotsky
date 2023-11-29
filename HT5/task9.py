def modify_list(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 != 0:
            del lst[i]
        else:
            lst[i] //= 2
            i += 1


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
modify_list(numbers)
print(numbers)
