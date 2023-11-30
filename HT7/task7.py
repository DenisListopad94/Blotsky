try:
    index_test = [1, 2, 3]
    print(index_test[4])
except IndexError as error:
    print(f"error: {error}")
