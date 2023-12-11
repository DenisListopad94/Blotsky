def roman_to_integer(s):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0
    prev_value = 0

    for char in s:
        value = roman_values[char]

        if prev_value < value:
            result += value - 2 * prev_value
        else:
            result += value

        prev_value = value

    return result


input_1 = "III"
input_2 = "LVIII"
input_3 = "MCMXCIV"

output_1 = roman_to_integer(input_1)
output_2 = roman_to_integer(input_2)
output_3 = roman_to_integer(input_3)

print(f"Sample Input 1: {input_1}")
print(f"Sample Output 1: {output_1}")

print(f"Sample Input 2: {input_2}")
print(f"Sample Output 2: {output_2}")

print(f"Sample Input 3: {input_3}")
print(f"Sample Output 3: {output_3}")
