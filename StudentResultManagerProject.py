student = {}

while True:
    print("----Student Result Manager----")
    print("1. Add student")
    print("2. View students")
    print("3. Check result")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        marks = int(input("Enter your marks: "))
        student[name] = marks
        print(f"{name} successfully added!")
    elif choice == 2:
        if not student:
            print("Student not found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)
    elif choice == 3:
        name = input("Enter the name: ")

        if name in student:
            marks = student[name]

            if marks >= 40:
                print("Pass")
            else:
                print("Fail")
        else:
            print("Student not found!")        
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid! input")