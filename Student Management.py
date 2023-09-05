def accept_students():
    students = []
    for i in range(2):
        name = input("Enter student Name: ")
        age = input("Enter student age: ")
        Rollno = input("Enter student Rollno:")
        students.append({"name": name, "age": age, "Rollno": Rollno})
    return students

def display_students(students):
    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Rollno:", student["Rollno"])
        print()

def search_student(students, name):
    for student in students:
        if student["name"] == name:
            return student
    return None

def delete_student(students, Rollno):
    for student in students:
        if student["Rollno"] == Rollno:
            students.remove(student)
            return True
    return False

students = accept_students()

display_students(students)

search_name = input("Enter the Name of the student to search for :- ")
found_student = search_student(students, search_name)
if found_student:
    print("Student found:")
    print("Name:", found_student["name"])
    print("Age:", found_student["age"])
    print("Rollno:", found_student["Rollno"])
else:
    print("Student not found.")

delete_rollno = input("Enter the Roll number of the student to delete :- ")
if delete_student(students, delete_rollno):
    print("Student deleted successfully.")
else:
    print("Student not found.")

display_students(students)