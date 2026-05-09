
def show_balance():
    print(f"Your balance is {balance}")

def deposit():
    amount = int(input("Enter your amount: "))
    if amount < 0:
        print("Not valid")
        return 0
    else:
        return amount

def withdraw():
    amount = int(input("Enter your amount: "))
    if amount > balance:
        print("Insufficient")
        return 0
    elif amount <= 0:
        print("Amount must be greater than 100")
        return 0
    else:
        return amount
    

balance = 0
while True:
    print("<<==Bank System==>>")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4.Exit Program")
    
    choose = int(input("Enter your choice: "))

    if choose == 1:
        show_balance()

    elif choose == 2:
        balance += deposit()
    elif choose == 3:
        balance -= withdraw()
    elif choose == 4:
        print("Exit Program")
        break
    else:
        print("Invalid")
print("Thank you")    
