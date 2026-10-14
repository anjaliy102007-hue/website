# Greeting Function

# def greet(name):
#     print("Welcome,",name)

# name =input("Enter student's name:")   
# greet(name) 

# Addition Function

# def add(a,b):
#     return a + b 

# x = int(input("Enter first number:"))
# y = int(input("Enter second number:"))

# print("Sum=", add (x,y))

# Even or odd

# def check_even_odd(n):
#     if n % 2 == 0:
#         return"Even"
#     else:
#         return"odd"

# num = int(input("Enter an integer:"))
# print(check_even_odd(num))    

# Factorial Calculator

# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result*=i
#         return result

# num=int(input("Enter a non-negative integer:"))

# if num >= 0:
#     print("Factorial=",factorial(num))
# else:
#     print("Invalid input")    
            
# Largest of Three Numbers

# def largest(a,b,c):
#     return max(a,b,c)

# x = int(input("Enter first number:"))
# y = int(input("Enter second number:")) 
# z = int(input("Enter thrid number:")) 

# print("Largest number =", largest(x,y,z))

# Grade Calculator
# Grade boundaries used: 90–100 = A, 75–89 = B, 60–74 = C, 40–59 = D, below 40 = F.

# def calcualate_grade(marks):
#     if marks >= 90:
#         return"A"
#     elif marks >= 75:
#         return "B"
#     elif marks >= 60:
#         return "C"
#     elif marks >= 40:
#         return "D"
#     else:
#         return "F"

# marks = int(input("Enter marks (0-100):"))

# if 0 <= marks <=100:
#     print("Grade =", calcualate_grade(marks))
# else:
#     print("Invalid marks")

# List Statistics

# def total(numbers):
#     return sum(numbers)

# def average(numbers):
#     return sum(numbers) / len(numbers)

# def minimum(numbers):
#     return min(numbers)

# def maximun(numbers):
#     return max(numbers)

# numbers = [10,20,30,40,50]

# print("Total =", total(numbers))
# print("Average =", average(numbers))
# print("Minimum=", minimum(numbers))
# print("Maximum=", maximun(numbers))

# Banking Application

# def deposit(balance, amount):
#     balance +=amount
#     print(f"Deposited {amount}. New balance is {balance}")
#     return balance

# def withdraw(balance,amount):
#     if amount > balance:
#         print("Insufficient balance")
#     else:
#         balance -=amount
#     return balance

# def display_balance(balance):
#     print(f"Current balance is {balance}")

# balance= 0

# while True:
#     print("\n Bankig Menu")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Display balance")
#     print("4. Exit")

#     choice=input("Enter your choice :")
#     if choice == "1":
#         amt=float(input("Enter amount to deposit:"))
#         balance = deposit(balance, amt)
#     elif choice =="2":
#         amt=float(input("Enter amount to withdraw:"))
#         balance = withdraw(balance, amt)
#     elif choice =="3":
#         display_balance(balance)
#     elif choice =="4":
#         print("Thank you for banking with us!")
#     else:
#         print("Invalid choice. Please try again.")

# Student Record processor

# students = [
#     {"name": "Rahul", "marks": [80, 75, 90]},
#     {"name": "Priya", "marks": [65, 70, 60]},
#     {"name": "Aman", "marks": [30, 35, 25]},
#     {"name": "Neha", "marks": [85, 90, 95]}
# ]

# def calculate_average(marks):
#     return sum(marks) / len(marks)

# def passing_students(students):
#     for student in students:
#         avg = calculate_average(student["marks"])
#         if avg >= 40:
#             print(student["name"], "- Average:", avg)

# print("Passing Students:")
# passing_students(students)