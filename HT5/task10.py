def generate_sequence(n):
    sequence = []
    current_number = 1

    for i in range(n):
        for j in range(i + 1):
            sequence.append(current_number)

        current_number += 1

    return sequence


n = int(input("Введите число n: "))

result_sequence = generate_sequence(n)
print(*result_sequence)
