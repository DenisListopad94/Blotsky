def add_contact(phonebook, name, *phone_numbers):
    if name in phonebook:
        phonebook[name].extend(phone_numbers)
    else:
        phonebook[name] = list(phone_numbers)


def print_phonebook(phonebook):
    for name, numbers in phonebook.items():
        print(f"{name}: {', '.join(map(str, numbers))}")


phonebook = {}

add_contact(phonebook, "Коля", "123-456-789")
add_contact(phonebook, "Петя", "987-654-321")
add_contact(phonebook, "Коля", "8-800-555-3535", "444-555-666")

print_phonebook(phonebook)
