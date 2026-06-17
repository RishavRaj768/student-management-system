# Student managemant system
import os

FILE_NAME = "students.txt"

# Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{course}\n")

    print("Student Added Successfully!")

# View Students
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found!")
        return

    print("\n--- Student Records ---")
    with open(FILE_NAME, "r") as file:
        records = file.readlines()

        if not records:
            print("No records available!")
            return

        for record in records:
            roll, name, course = record.strip().split(",")
            print(f"Roll: {roll} | Name: {name} | Course: {course}")

# Search Student
def search_student():
    roll_no = input("Enter Roll Number to Search: ")

    found = False

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for record in file:
                roll, name, course = record.strip().split(",")

                if roll == roll_no:
                    print("\nStudent Found!")
                    print(f"Roll: {roll}")
                    print(f"Name: {name}")
                    print(f"Course: {course}")
                    found = True
                    break

    if not found:
        print("Student not found!")

# Update Student
def update_student():
    roll_no = input("Enter Roll Number to Update: ")

    updated_records = []
    found = False

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for record in file:
                roll, name, course = record.strip().split(",")

                if roll == roll_no:
                    print("Enter New Details")
                    name = input("New Name: ")
                    course = input("New Course: ")
                    found = True

                updated_records.append(f"{roll},{name},{course}\n")

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_records)

        if found:
            print("Student Updated Successfully!")
        else:
            print("Student not found!")

# Delete Student
def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")

    records = []
    found = False

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for record in file:
                roll, name, course = record.strip().split(",")

                if roll != roll_no:
                    records.append(record)
                else:
                    found = True

        with open(FILE_NAME, "w") as file:
            file.writelines(records)

        if found:
            print("Student Deleted Successfully!")
        else:
            print("Student not found!")

# Main Menu
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Please Try Again.")