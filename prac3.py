# Prepaid college Canteen Card System
Balance=500
Pin=4321

# Pinchecking
for i in range(3):
    user_pin = int(input("Enter pin:"))

    if user_pin == Pin:
        print("Login Sucessful")
        break
    else:
        print("card Blocked")
        exit()

# menu
while True:
    print("check Balance")
    print("Recharge")
    print("Make Purchase")
    print("view transaction history")
    print("exit")

    choice = int(input("enter your choice:"))

    if choice == 1:
        print("Balance:",Balance)

    elif choice ==2:
        amount = int(input("enter recharge amount:"))
        if amount <=0:
            print("Invalid Amount")
            continue

        Balance = Balance + amount
        print("recharge sucessful")
        print("New Balance:", Balance)  

    elif choice ==3:
        amount = int(input("enter purchase amount:"))

        if amount <= 0:
            print("Invalid amount")
            continue

        elif amount > Balance:  
            print("Insufficient Balance")
        else:
            Balance = Balance - amount
            print("purchase successful")
            print("remaining balance:",Balance)   
    elif choice == 4:
        pass

    elif choice == 5:
        print("final balance:",Balance)
        break

    else:
        print("Invalid choice")