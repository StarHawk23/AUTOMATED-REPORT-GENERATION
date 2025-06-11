import csv

data = []
with open("students.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Get header
    for row in reader:
        data.append(row)
print(data)