import math


def write_file():
    file = open("Files/input.txt", 'w')

    for i in range(1, 11):
        file.write(str(i) + " ")
    file.close()


def read_file_sum():
    file_input = open("Files/input.txt")
    prov = file_input.read().split()
    prov2 = list(map(int, prov))
    print(math.prod(prov2))
    file_input.close()

    file_output = open("Files/output.txt", "w")
    file_summed = math.prod(prov2)
    file_output.write(str(file_summed))
    file_output.close()


write_file()
read_file_sum()
