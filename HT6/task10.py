def generate_permutations(n, current_permutation=[]):
    if len(current_permutation) == n:
        print(*current_permutation)
        return

    for num in range(1, n + 1):
        if num not in current_permutation:
            generate_permutations(n, current_permutation + [num])


n = int(input("Введите число n: "))

generate_permutations(n)
