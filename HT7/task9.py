try:
    file_input = open("Files/123123.txt")
    prov = file_input.read()
    print(prov)
except FileNotFoundError as error:
    print(f"Error: {error}")
