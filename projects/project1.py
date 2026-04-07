import json

students = []

# 🔹 Load data from file
def load_data():
    global students
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
    except:
        students = []

# 🔹 Save data to file
def save_data():
    with open("students.json", "w") as f:
        json.dump(students, f)

# 🔹 Add student
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    save_data()  # auto save
    print("Student added & saved")

# 🔹 View students
def view_std():
    if not students:
        print("No students found")
    else:
        for s in students:
            print("\nName:", s["name"])
            print("Age:", s["age"])
            print("Marks:", s["marks"])
            print("------")


# 🔹 Start program
load_data()

# MENU
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        view_std()
    elif ch == "3":
        break
    else:
        print("Invalid shit bitch")