def find_minimum_slices(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return (a * b) // gcd(a, b)


a = int(input("Введите размер команды биологов (a): "))
b = int(input("Введите размер команды информатиков (b): "))

result = find_minimum_slices(a, b)
print(f"Минимальное число кусочков пирога: {result}")
