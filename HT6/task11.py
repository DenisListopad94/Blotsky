def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binomial_coefficient(n - 1, k) + binomial_coefficient(n - 1, k - 1)


n, k = map(int, input("Введите значения n и k через пробел: ").split())

result = binomial_coefficient(n, k)
print(result)
