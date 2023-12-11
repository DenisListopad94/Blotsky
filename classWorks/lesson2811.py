# def get_student_info(*args, name: str = "Oleg", age: int = 0, **kwargs) -> None:
#     info = f"name: {name} age: {age} numbers {args} professors: {kwargs}"
#     return info
# 
# 
# print(get_student_info(3, 2, 5, name="Denis", age=22, math="filip", phys="mark"))

# def some_func(marks: list = []):
#     marks.append(3)
#     print(marks)
# 
# 
# some_func()
# some_func()

# def registration() -> None:
#     name = input("enter your name in upper case: ")
#     password = input("enter difficult password, min 4 sign ")
#     if not name.isupper():
#         raise ValueError(f"name: {name} in is not upper case:")
#     if len(password) < 4:
#         raise ArithmeticError(f" password: {password}min 4 need for password")
# 
# 
# while True:
#     try:
#         registration()
#     except ValueError as e:
#         print(e)
#         print("put data: ")
#         continue
#     else:
#         print("hi daun")
#         break

# try:
#     file = open(file="test.txt", mode="w", encoding="utf-8")
#     file.write("привет мир\n")
#     file.write(str(28))
# except FileExistsError:
#     print("error")
# finally:
#     if 'file' in locals():
#         file.close()

# file = open(file="test.txt", encoding="utf-8")
# data = file.read().split("\n")
# data = list(map(int, data))
# print(sum(data) / len(data))
# file.close()
# ages = []


# def read_data():
#     with open(file="test.txt", encoding="utf-8") as file:
#         counter = 0
#         for i in file:
#             if counter == 4:
#                 raise ValueError
#             ages.append(int(i.rstrip()))
#             counter += 1
#             print(i, end="")
# 
# 
# try:
#     read_data()
# except Exception:
#     print("sorry")
# 
# finally:
#     print(ages)

import json

student_info = {
    "name": "Oleg",
    "age": 28
}

# with open("student.json", "w") as file:
#     json.dump(student_info, file)
#     
with open("student.json", "r") as file:
    date = json.load(file)
print(type(date))
