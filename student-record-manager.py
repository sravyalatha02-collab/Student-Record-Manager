import re

FILE_NAME = "students.txt"


# Validate email using Regex
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(pattern, email):
        return True
    return False


# Add Student
def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        email = input("Enter Student Email: ")
        age = int(input("Enter Student Age: "))

        if name.strip() == "":
            raise ValueError("Name cannot be empty.")

        if age <= 0:
            raise ValueError("Age must be greater than 0.")

        if not validate_email(email):
            raise ValueError("Invalid email format.")

        with open(FILE_NAME, "a") as file:
            file.write(f"{student_id},{name},{email},{age}\n")

        print("Student added successfully!")

    except ValueError as e:
        print("Invalid input:", e)

    except Exception as e:
        print("Error:", e)


# Read Student Data
def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

            if len(students) == 0:
                print("No student records found.")
                return

            print("\nStudent Records")
            print("---------------------------")

            for student in students:
                data = student.strip().split(",")

                print("Student ID :", data[0])
                print("Name       :", data[1])
                print("Email      :", data[2])
                print("Age        :", data[3])
                print("---------------------------")

    except FileNotFoundError:
        print("No student file found.")


# Main Program
while True:

    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. Read Student Data")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            read_students()

        elif choice == 3:
            print("Program exited.")
            break

        else:
            print("Please enter a number between 1 and 3.")

    except ValueError:
        print("Invalid input. Please enter a number.")