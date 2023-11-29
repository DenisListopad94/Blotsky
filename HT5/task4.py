def calculate_neighbors_sum(numbers):
    if len(numbers) == 1:
        return numbers

    result = [numbers[i - 1] + numbers[(i + 1) % len(numbers)] for i in range(len(numbers))]
    return result


input_numbers = list(map(int, input("список чисел через пробел: ").split()))
output_result = calculate_neighbors_sum(input_numbers)
print(" ".join(map(str, output_result)))
