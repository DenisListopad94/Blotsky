def input_value(func):
    def wrapper():
        password = input("Enter your password ")
        func(password)

    return wrapper


@input_value
def check_password(password):
    if password == "admin":
        print("Welcome Admin")
    elif password == "user":
        print("Welcome User")
    else:
        print("get out here")


check_password()
