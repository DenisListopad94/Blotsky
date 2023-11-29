def digits(n):
    if n == 0:
        return
    else:
        digit = n % 10
        print(digit, end=" ")
        digits(n // 10)


input_date = 14623
digits(input_date)
