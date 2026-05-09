import random
data = {
"rizwanali05": "@Rizwan1231"
}
print("<<--- OTP Verification System --- >>")

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in data:
        if data[username] == password:
            random_number = random.randint(1000, 9999)
            print("Your OTP is:",random_number)
            otp = int(input("Enter your OTP: "))
            if random_number == otp:
                print("Login Successfully")
                print("Welcome Rizwan 👋")
                break
            else:
                print("retry")
        else:
            print("Wrong password")
    else:
        print("Username not found!")
