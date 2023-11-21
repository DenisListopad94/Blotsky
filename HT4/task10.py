def format_phone_number(phone):
    return f"+{phone[0]}({phone[1:4]}){phone[4:7]}-{phone[7:9]}-{phone[9:]}"


def phone_book():
    contacts = {}

    while True:
        query = input().strip()

        if query == '.':
            break

        parts = query.split()
        name = parts[0]

        if len(parts) == 1:
            if name in contacts:
                print(format_phone_number(contacts[name]))
            else:
                print("Не найдено")
        elif len(parts) == 2:
            contacts[name] = parts[1]

    for name, phone in contacts.items():
        print(format_phone_number(phone))


phone_book()
