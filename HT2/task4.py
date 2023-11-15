# Дано двузначное число. Определить является ли сумма его цифр двузначным числом. (Ответ: Да/Нет)

n = 55

a = n // 10  
b = n % 10   

sum_of_digits = a + b

is_two_digit_sum = 10 <= sum_of_digits <= 99

if is_two_digit_sum:
    print("Да")
else:
    print("Нет")