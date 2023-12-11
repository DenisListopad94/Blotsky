def decompress_string(compressed_string):
    result = ""
    i = 0

    while i < len(compressed_string):
        char = compressed_string[i]

        if char.isalpha():
            result += char
            i += 1
        else:
            count = ""
            while i < len(compressed_string) and compressed_string[i].isdigit():
                count += compressed_string[i]
                i += 1

            if count:
                result += int(count) * compressed_string[i]
            i += 1

    return result


file_path = 'Files/12.txt'
with open(file_path, encoding='utf-8') as file:
    compressed_string = file.read()
    decompressed_string = decompress_string(compressed_string)
    print("Исходная строка:", decompressed_string)
