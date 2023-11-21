numbers = [7, 4, 1]

print(*sum(([n, 0] if i < len(numbers) - 1 else [n] for i, n in enumerate(numbers)), []))
