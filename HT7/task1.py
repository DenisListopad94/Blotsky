def write_file():
    file = open("Files/test1.txt", "w")
    for i in range(100):
        file.write(str(i) + " text " + "!" + "\n")
    file.close()


def read_file():
    with open("Files/test1.txt", "r") as f:
        print(f.read())


# Файл закрыть не трубуется, тк в конструкции with он сам закрывается

write_file()
read_file()
