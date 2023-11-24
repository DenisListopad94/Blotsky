try:
    a = input("Введи свое имя с главном буквы: ")

    n = lambda x: x[0].isupper()
    result = n(a)

    if result:
        print(f"{a} start from capital latter")
    else:
        print(f"{a} name doesn't start from capital latter")
except IndexError:
    print("Введи имя, поле не может быть пустым и не может содержать специальных символов: ")
