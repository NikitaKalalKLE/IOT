# Function to calculate total marks
def calculate_total_marks(student):
    name, maths, vlsi, python = student
    total = maths + vlsi + python
    return name, total


# List of student scores (name, maths, VLSI, Python)
students = [
    ("Alice", 85, 90, 78),
    ("Bob", 70, 88, 92),
    ("Charlie", 95, 85, 80),
    ("David", 60, 75, 70)
]
for student in students:
    student["total"] = student["maths"] + student["vlsi"] + student["python"]

# Print updated list
for s in students:
    print(s)


# Calculate and display totals
for student in students:
    name, total = calculate_total_marks(student)
    print(f"{name} - Total Marks: {total}")
