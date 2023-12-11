def find_prime_divisors(n, divisor=2):
    if n <= 1:
        return []

    divisors = []

    while divisor <= n:
        if n % divisor == 0:
            divisors.append(divisor)
            return divisors + find_prime_divisors(n // divisor, divisor)
        divisor += 1

    return divisors


n = int(input("Введите натуральное число n (n > 1): "))

prime_divisors = find_prime_divisors(n)
print(*prime_divisors)
