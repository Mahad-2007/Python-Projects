print("<<----WELCOME TO THEME PARK!---->>")
print("<<-----ENJOY EVERY MOMENT!----->>")


Entry = []
name = input("Enter your name: ")
age = int(input("Enter your age: "))
balance = int(input("Enter your balance: "))

total_price = 0
selectfood = 0
selectitem = 0

user = {
    "name": name,
    "age": age,
    "balance": balance
}


def check_balance(total_price, balance):
    if total_price > balance:
        print("Apka balance pura ho gaya hai! Ab aap mazeed kuch nahi kar sakte. Ghar chale jao beta 😄")
        exit()


if user["age"] >= 3 and user["age"] <= 7:
    user["price"] = 500
elif user["age"] > 7 and user["age"] <= 18:
    user["price"] = 1000
elif user["age"] > 18 and user["age"] <= 40:
    user["price"] = 1500
else:
    print("Invalid!")

for each in user.items():
    Entry.append(each)

for i in Entry:
    print(i)


games = {
    500: ["1. Zoo", "2. Roller Coaster", "3. Quirim Hall"],
    1000: ["1. Swimming Pool", "2. Wave Pool"],
    2000: ["1. Heavy Rides"]
}


def getResponse(additional_game):
    if additional_game in games:
        return games[additional_game]
    else:
        return "Package not found!"


while True:
    userInput = input("Enter your range (or type OK to exit): ")

    if userInput.lower() == "ok":
        break

    try:
        userInput = int(userInput)
        reply = getResponse(userInput)
        print("Response:", reply)

        select = input("Select your game: ")
        total_price = user["price"] + userInput
        check_balance(total_price, balance)

        print("Total Price:", total_price)
        break

    except:
        print("Please enter a valid number!")


foods = {
    500: "KFC",
    1000: "McDonald's"
}

food = input("Would you like to eat something? (Yes/No): ")
if food.lower() == "yes":
    print(foods)
    selectfood = int(input("Select your food: "))
    total_price = total_price + selectfood
    check_balance(total_price, balance)

    print("Total Price:", total_price)

else:
    print("Your total bill:", total_price)


fashions = {
    500: "Makeup",
    1000: "Dress"
}

faishon = input("Would you like to buy some fashion accessories? (Yes/No): ")
if faishon.lower() == "yes":
    print(fashions)
    selectitem = int(input("Select your item: "))
    total_price = total_price + selectitem
    check_balance(total_price, balance)

    print("Total Price:", total_price)

else:
    print("Your total bill:", total_price)


full_bill = input("Would you like to see the full bill? (Yes/No): ")
if full_bill.lower() == "yes":
    total_bill = total_price

    print("Your total bill:", total_bill)
    checkbalace = balance - total_bill
    print("Remaining balance:", checkbalace)