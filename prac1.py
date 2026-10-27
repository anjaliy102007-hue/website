# Age Verification System

# try:
#     age = int(input("Enter your age:"))

#     if age < 0 or age > 120:
#         raise ValueError("Age must be between 0 and 120.")

#     print("Valid age:", age)

# except ValueError as e:
#     print("Error:",e)    

# Product Price Checker

# try:
#     price = float(input("Enter product price:"))

#     if price < 0:
#         raise ValueError("Price cannot be negative.")

#     print("Product price:", price)

# except ValueError as e: 
#     print("Invalid price:",e)    

# Tuple Element Access

# cities = ("Delhi","Mumbai","lucknow","Chennai","kolkata","Jaipur","Bhopal")

# try:
#     position = int(input("Enter postiion(0-6):"))
#     print("city:", cities[position])

# except IndexError:
#     print("Error: Position is out of range. ")

# except ValueError:
#     print("Error : Please enter an integer.")    

# Contact Information Lookup

# contacts = {
#     "Rahul": "9876543210",
#     "Aman": "9876501234",
#     "Priya": "9123456780"
# }

# try:
#     name = input("Enter contact name: ")
#     print("Phone number:", contacts[name])

# except KeyError:
#     print("Error: Contact not found.")

# File Writing Operation

# try:
#     filename = input("Enter filename:")
#     text = input("Enter text to write:")

#     with  open(filename, "w") as file:
#         file.write(text)

#     print("Text written successfully.")

# except PermissionError:
#     print("Error: Permission denied.")

# except OSError as e:
#     print("File error:",e)

# Valid Roll Number Input

# while True:
#     try:
#         roll = int(input("Enter student roll number: "))

#         if roll <= 0:
#             print("Roll number must be greater than zero.")
#             continue

#         print("Valid roll number:", roll)
#         break

    # except ValueError:
        # print("Invalid input. Enter an integer.")

# Custom Exception for Voting Eligibility

# class NotEligibleToVoteError(Exception):
#     pass

# try:
#     age = int(input("Enter your age:"))

#     if age < 18:
#         raise NotEligibleToVoteError(
#             "You are not eligible to vote."
#         )

#     print("You are eligible to vote.")

# except ValueError:
#     print("Please enter a valid age.")

# except NotEligibleToVoteError as e:
#     print(e)

# Bank Account Deposit Validation

# try:
#     amount = float(input("Enter deposit amount:"))

#     if amount <= 0:
#         raise ValueError("Deposite must be grater than zero.")

#     print("Deposite successful:",amount)

# except ValueError as e:
#     print("Error:,e")    

# Shopping Cart Quantity Check

# try:
#     quantity = int(input("Enter item quantity: "))

#     if quantity < 1:
#         raise ValueError("Quantity must be at least 1.")

#     print("Quantity added:", quantity)

# except ValueError as e:
#     print("Error:", e)

# Password Strength Validator

# try:
#     passoword = input("enter password:")

#     if len (passoword) < 8:
#         raise ValueError(
#             "Password must contain at least 8 characters."
#         )

#     print("Password accepted.")

# except ValueError as e:
#     print("Error:",e)    

