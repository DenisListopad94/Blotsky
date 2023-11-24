def is_power(n):
    if n == 1:
        return True
    elif n % 2 != 0 or n == 0:
        return False
    else:
        return is_power(n // 2)


input_number = 1048576
output_result = is_power(input_number)
print(output_result)
