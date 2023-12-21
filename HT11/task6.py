def pascal_triangle(n):
    triangle = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                triangle[i][j] = 1
            else:
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle


def print_pascal_triangle(triangle):
    for row in triangle:
        print("   ".join(map(str, row)))


n = 8
triangle = pascal_triangle(n)
print_pascal_triangle(triangle)

# Не решил и в гугле не смог найти решение
