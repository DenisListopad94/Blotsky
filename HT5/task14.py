import re


def check_variable(variable):
    if variable[0].isdigit():
        return "Нельзя использовать"

    if re.search(r'[^\w_]', variable):
        return "Нельзя использовать"

    return "Можно использовать"


while True:
    variable_name = input("Введите имя переменной (или 'Поработали, и хватит' для завершения): ")

    if variable_name == 'Поработали, и хватит':
        break

    result = check_variable(variable_name)
    print(result)
