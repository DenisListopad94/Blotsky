# Найти количество четных чисел среди заданных трех целых чисел.В ответе вывести количество четных чисел.

num1 = 2
num2 = 13
num3 = 22

for i in num1, num2, num3:
    if i % 2 ==0:
        print("Even number: ", i)
    if i % 2 != 0:
        print("Is not even number: ", i)