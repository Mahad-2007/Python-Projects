users = {}

while True:
    print("<<---Login + Signup System--->>")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        username = input("Enter your name: ")
        if username in users:
            print("username already exists!")
        else:
            password = input("Enter your password: ")
            users[username] = password
            print("Account created successfully!")
    elif choice == "2":
        username = input("Enter your name: ")
        password = input("Enter your password: ")
        
        if username in users:
            if users[username] == password:
                print("Login Successfuly!")
            else:
                print("Wrong password")
        else:
            print("Username not found!")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid!")