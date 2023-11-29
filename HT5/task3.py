def sum_in_st(num1, num2, num3):
    entered_num = [num ** num3 for num in range(num1, num2 + 1)]
    return entered_num


num1, num2, num3 = map(int, input("Введи начало, конец и степень через пробел(3 числа): ").split())
result = sum_in_st(num1, num2, num3)
print(result)
