import json

value_dict = {
    12345: ("apple", 25),
    34566: ("amazon", 33),
    54321: ("jbl", 43),
    23122: ("samsung", 23),
    11111: ("google", 343)
}
try:
    with open("Files/valueTsk4.json", "w") as gg:
        json.dump(value_dict, gg)
    print("File recorded")

except Exception as e:
    print(f"Can't recorded, error: {e}")
