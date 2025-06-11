import csv

# Correct student data
students = [
    ["Name", "Roll No", "Marks"],
    ["Sriram", 101, 95],
    ["Lokesh", 102, 90],
    ["Shaleem", 103, 98],
    ["Navaneeth", 104, 100],
    ["Vishnu", 105, 99],
    ["Ganesh", 106, 97],
    ["Vamsi", 107, 92]
]

# Write to CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("✅ students.csv file created successfully!")
