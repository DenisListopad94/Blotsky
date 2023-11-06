cash = int(input("Введите сумму для оплаты: "))

hundred_rubles = cash // 100
cash %= 100
fifty_rubles = cash // 50
cash %= 50
ten_rubles = cash // 10
one_ruble = cash % 10

print(f"{hundred_rubles} купюр по 100 рублей")
print(f"{fifty_rubles} купюр по 50 рублей")
print(f"{ten_rubles} купюр по 10 рублей")
print(f"{one_ruble} купюр по 1 рублю")
