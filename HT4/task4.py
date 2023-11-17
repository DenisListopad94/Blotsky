numbers = [18, 42, 8, 122]

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        reversed_str = str(numbers[i])[::-1]
        numbers.insert(i + 1, int(reversed_str))

print(numbers)
