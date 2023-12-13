def is_perfect_number(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisors_sum == num


def perfect_numbers_generator(limit):
    current = 2
    while current <= limit:
        if is_perfect_number(current):
            yield current
        current += 1


try:
    for perfect_num in perfect_numbers_generator(1000000000):
        print(perfect_num, end=' ')
except StopIteration:
    pass
