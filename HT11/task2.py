def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def simple(n):
    current = 2
    while current <= n:
        if is_prime(current):
            yield current
        current += 1


try:
    for prime_num in simple(20):
        print(prime_num, end=' ')
except StopIteration:
    pass  
