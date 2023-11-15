# Дано 3 числа. Напишите программу, которая выводит True, если хотя бы одно из чисел А, В, С отрицательно. Если нет вывести False.

nums1 = 1
nums2 = -2
nums3 = 1
numberFlag1 = True
numberFlag2 = True

for i in nums1, nums2, nums3:
    if i < 0:
        numberFlag1 = False
        print(numberFlag1, i)
    if i > 0:
        print(numberFlag2, i)
