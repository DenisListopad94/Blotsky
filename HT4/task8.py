n = int(input())
possible_numbers = set(range(1, n + 1))

result = sorted(possible_numbers)
print(*result)
