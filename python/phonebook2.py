import csv

data = {
    "Name": None,
    "Number": None
}

with open("phonebook2.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        name = row[0]
        number = row[0]
        data[name] = name
        data[number] = number

for name in data:
    print(f"Name: {data[name]}, Number: {data[number]}")
