def after_recursive(s, index=0):
    if index == len(s):
        return 0
    else:
        digit = int(s[index])
        return digit + after_recursive(s, index + 1)


num = "14623"
result = after_recursive(num)
print(result)
