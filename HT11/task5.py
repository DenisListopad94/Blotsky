class Server:
    def __init__(self):
        self.data = []

    def process_command(self, command):
        if command.startswith("POST"):
            _, value = command.split(maxsplit=1)
            self.data.append(value)
            return f"Added: {value}"

        elif command == "GET":
            if self.data:
                return f"Last added: {self.data[-1]}"
            else:
                return "Server is empty"

        elif command == "DELETE":
            if self.data:
                deleted_value = self.data.pop()
                return f"Deleted: {deleted_value}"
            else:
                return "Server is empty"

        else:
            return "Unknown command"


server = Server()
commands = [
    "POST 12",
    "POST 15",
    "POST 81",
    "GET",
    "DELETE",
    "DELETE",
    "POST Stack Overflow",
    "POST Recursion",
    "DELETE",
    "GET"
]

for command in commands:
    if command == ".":
        break
    result = server.process_command(command)
    print(result, end=" ")
