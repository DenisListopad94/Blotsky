def process_string(input_string):
    start_index = input_string.find('{')
    end_index = input_string.find('}', start_index)

    if start_index != -1 and end_index != -1 and start_index < end_index:
        processed_string = input_string[:start_index] + input_string[end_index + 1:]
    elif start_index != -1:
        processed_string = input_string[:start_index]
    else:
        processed_string = input_string

    most_common_char = max(set(processed_string), key=processed_string.count)

    return processed_string, most_common_char


input_str = "abc{def}gh{ij}kl"
processed_str, most_common = process_string(input_str)
print("Processed String:", processed_str)
print("Most Common Character:", most_common)
