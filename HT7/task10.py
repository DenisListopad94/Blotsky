unknown_list = [1, 2, 3]
try:
    el = int(input("Напиши какое число удалить из списка: "))
    if el == 1:
        del unknown_list[0]
        print(f"число {el} было удалено из списка")
    elif el == 2:
        del unknown_list[1]
        print(f"число {el} было удалено из списка")
    elif el == 3:
        del unknown_list[2]
        print(f"число {el} было удалено из списка")
        print(unknown_list)
    else:
        raise TypeError
except TypeError as error:
    print(f"Error: you can't remove don't exist number ")
