import csv
import json


def read_file():
    with open("Files/items.json", "r") as file_json:
        data = json.load(file_json)

    with open("Files/items.csv", "w", newline="") as cs_file:
        fields = list(data[0].keys())

        fields_with_prefix = ["# " + fields[0]] + fields[1:]

        writer = csv.writer(cs_file)
        writer.writerow(fields_with_prefix)

        for row in data:
            row_with_prefix = ["person; " + str(value) if i == 0 else value for i, value in enumerate(row.values())]
            writer.writerow(row_with_prefix)
    print(data)
    file_json.close()


read_file()
