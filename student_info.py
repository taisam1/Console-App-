import sqlite3

print("Enter a to d to select option")
print("------------------------------")
print("a. Add new student information")
print("b. Retrieve all student information")
print("c. Update student information")
print("d. Delete student information")

option = input("Select an option (a-d): ")


if option.lower()== "a":
    matric_number = input("Enter your matric number: ")
    email = input("Enter your email address: ")
    department = input("Enter your department: ")
    age = int(input("Enter your age: "))
    faculty = input("Enter your faculty: ")

    with sqlite3.connect("student_info.db") as conn:
        cursor = conn.cursor()

        sql = """
        INSERT INTO students
        (matric_number, email, department, age, faculty)
        VALUES (?, ?, ?, ?, ?)
        """

        cursor.execute(sql, (matric_number, email, department, age, faculty))
        conn.commit()

    print("Student information inserted successfully.")

elif option.lower() == "b":
    with sqlite3.connect("student_info.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        if students:
            print("\nStudent Information:")
            for student in students:
                print(f"Matric Number: {student[1]}")
                print(f"Email: {student[2]}")
                print(f"Department: {student[3]}")
                print(f"Age: {student[4]}")
                print(f"Faculty: {student[5]}")
        else:
            print("No students found.")
elif option.lower() == "c":
    matric_number = input("Enter the matric number of the student to update: ")
    new_email = input("Enter the new email address: ")
    new_department = input("Enter the new department: ")
    new_age = int(input("Enter the new age: "))
    new_faculty = input("Enter the new faculty: ")
    sql = """
        INSERT INTO students(matric_number, email, department, age, faculty) 
        VALUES(?, ?, ?, ?, ?)
        """
        

    with sqlite3.connect("student_info.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE students
            SET email = ?, department = ?, age = ?, faculty = ?
            WHERE matric_number = ?
        """, (new_email, new_department, new_age, new_faculty, matric_number))
        if cursor.rowcount > 0:
            print("Student information updated successfully.")
        else:
            print("No student found with that matric number.")
elif option.lower() == "d":
    matric_number = input("Enter the matric number of the student to delete: ")

    with sqlite3.connect("student_info.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE matric_number = ?", (matric_number,))
        if cursor.rowcount > 0:
            print("Student information deleted successfully.")
        else:
            print("No student found with that matric number.")
else:
    print("Invalid option selected. Please choose a valid option (a-d).")

with sqlite3.connect("student_info.db") as  conn:
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS 
    students(
    id INTEGER PRIMARY KEY,
    matric_number TEXT UNIQUE,
    email TEXT,
    department TEXT,
    age INTEGER,
    faculty TEXT
    )
    """)