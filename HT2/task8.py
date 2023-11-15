# Дано число n. Вывести на экран числа 1, 4, 9, 16, 25, ... которые меньше n.
# Sample Input :
# 15
# Sample Output :
# 1 4 9

n = int(input("Введите число n: "))

i = 1
while i**2 < n:
    print(i**2, end=" ")
    i += 1