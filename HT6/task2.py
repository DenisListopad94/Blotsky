lst = {1, 2, 3, 4, 5, 6, 7, 8}

n = lambda x: x in lst and x % 2 == 0

result = filter(n, lst)
print(list(result))
