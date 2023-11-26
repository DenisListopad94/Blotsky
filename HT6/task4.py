def after_recursive(n):
    if n == 0:
        return
    else:
        digit = n % 10
        print(digit, end=" ")
        after_recursive(n // 10)


input_date = 14623
after_recursive(input_date)
