def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


n = int(input("Введите целое неотрицательное число n: "))
result = fib(n)
print(f"{n}-е число Фибоначчи: {result}")
