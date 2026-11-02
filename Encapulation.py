# class Employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self._salary = salary

#     def get_salary(self):
#         return self._salary

#     def inc_salary(self,amount):
#         if amount >0:
#             self._salary += amount
#             print("salary updated") 
#         else:
#             print("Invalid amount")

# emp=Employee("Anjali",25,50000) 
# print("Salary:",emp.get_salary())

# emp.inc_salary(8000)
# print("New Balance:",emp.get_salary())
# --------------------------------------------------------------------
# inheritance

# single inheritance

# class Animal():
#     def property(self):
#         print("Animal has 4 legs")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# d=Dog() 

# d.property()
# d.bark()

# multiple inheritance

# class Father():
#     def skill1(self):
#         print("Driving")

# class Mother():
#     def skills2(self):
#         print("Cooking")

# class child(Father,Mother):
#     def Qualities(self):
#         print("Inherited skills from parents:")

# x=child()
# x.Qualities()
# x.skill1()
# x.skills2()                        

# multilevel inheritance

# class Grandfather():
#     def house(self):
#         print("Grandfather's house")

# class Father(Grandfather):
#     def bike(self):
#          print("Father's bike")

# class Son(Father):
#     def laptop(self):
#          print("Son's Laptop")

# class Grandson(Son):
#     def car(self):
#          print("Grandson's car")
# g=Grandson()

# g.house()
# g.bike()
# g.laptop()
# g.car()

# # Hierarchical inheritance

# class Institute():
#     def name(self):
#         print("NSTIW Allahabad")

# class Teacher(Institute):
#     pass
# class Student(Institute):
#     pass
# class Housekeeping(Institute):
#     pass

# t=Teacher()
# s=Student()
# h=Housekeeping()

# s.name()
# t.name()
# h.name

# Student Management System (Single Inheritance)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# class Student(Person):
#     def __init__(self, name, age, roll_no, course):
#         super().__init__(name, age)
#         self.roll_no = roll_no
#         self.course = course

#     def display_student(self):
#         self.display_details()
#         print("Roll Number:", self.roll_no)
#         print("Course:", self.course)


# # Creating Student object
# s1 = Student("Anjali", 18, 101, "Artificial Intelligence")

# # Displaying student information
# s1.display_student()

# Bank Account System (Single Inheritance)
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited Amount:", amount)


# class SavingAccount(BankAccount):
#     def __init__(self, account_number, balance, interest_rate):
#         super().__init__(account_number, balance)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         return interest

#     def display_details(self):
#         print("Account Number:", self.account_number)
#         print("Balance:", self.balance)
#         print("Interest Rate:", self.interest_rate, "%")
#         print("Interest Earned:", self.calculate_interest())


# # Creating object
# account = SavingAccount(123456, 10000, 5)

# account.deposit(2000)
# account.display_details()

# Family Assets (Multilevel Inheritance)
# class Grandfather:

#   def house(self):
#     print("Grandfather's Asset: Ancestral House owned.")


# class Father(Grandfather):

#   def bike(self):
#     print("Father's Asset: Motorcycle owned.")


# class Son(Father):

#   def laptop(self):
#     print("Son's Asset: Gaming Laptop owned.")


# # Demonstration
# print("\n--- 3. Family Assets ---")
# son = Son()
# son.house()
# son.bike()
# son.laptop()

# Employee Hierarchy (Multilevel Inheritance)
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def get_name(self):
#         print("Employee Name:", self.name)


# class Employee(Person):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.emp_salary = salary

#     def salary(self):
#         print("Salary:", self.emp_salary)


# class Manager(Employee):
#     def __init__(self, name, salary, team_size):
#         super().__init__(name, salary)
#         self.team_size = team_size

#     def display_details(self):
#         self.get_name()
#         self.salary()
#         print("Team Size:", self.team_size)


# # Creating object
# manager = Manager("Avinash", 50000, 10)

# # Display information
# manager.display_details()

# College Management System (Hierarchical Inheritance)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Student(Person):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)
#         self.marks = marks

#     def display_student(self):
#         print("Student Details")
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Marks:", self.marks)


# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject

#     def display_teacher(self):
#         print("\nTeacher Details")
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Subject:", self.subject)


# # Creating objects
# s1 = Student("Rahul", 20, 85)
# t1 = Teacher("Priya", 30, "Python")

# # Display details
# s1.display_student()
# t1.display_teacher()

# Vehicle Management System (Hierarchical Inheritance)
# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")


# class Car(Vehicle):
#     def air_condition(self):
#         print("Car AC is ON")


# class Bike(Vehicle):
#     def helmet_required(self):
#         print("Helmet is required for Bike")


# class Bus(Vehicle):
#     def passenger_capacity(self):
#         print("Bus capacity is 50 passengers")


# # Creating objects
# c = Car()
# b = Bike()
# bus = Bus()

# # Calling methods
# c.start()
# c.air_condition()

# b.start()
# b.helmet_required()

# bus.start()
# bus.passenger_capacity()

# Smart Phone System (Multiple Inheritance)
# class Camera:
#     def take_photo(self):
#         print("Taking a photo")


# class MusicPlayer:
#     def play_music(self):
#         print("Playing music")


# class SmartPhone(Camera, MusicPlayer):
#     def make_call(self):
#         print("Making a phone call")


# # Creating object
# s = SmartPhone()

# # Calling all methods
# s.take_photo()
# s.play_music()
# s.make_call()

# Working Student (Multiple Inheritance)
# class Student:
#     def study(self):
#         print("Student is studying")


# class Employee:
#     def work(self):
#         print("Employee is working")


# class WorkingStudent(Student, Employee):
#     def manage_time(self):
#         print("Managing time between study and work")


# # Creating object
# w = WorkingStudent()

# # Calling all methods
# w.study()
# w.work()
# w.manage_time()


# Company Structure (Hybrid Inheritance)
# class Employee:
#     def attendance(self):
#         print("Employee attendance marked")


# class Developer(Employee):
#     def write_code(self):
#         print("Developer is writing code")


# class Tester(Employee):
#     def test_software(self):
#         print("Tester is testing software")


# class TeamLead(Developer, Tester):
#     def manage_team(self):
#         print("Team Lead is managing the team")


# # Creating object
# t = TeamLead()

# # Calling all methods
# t.attendance()
# t.write_code()
# t.test_software()
# t.manage_team()

# Educational Institute (Hybrid Inheritance)
# class Person:
#     def display_name(self):
#         print("Name: Rahul")


# class Student(Person):
#     def study(self):
#         print("Student is studying")


# class Teacher(Person):
#     def teach(self):
#         print("Teacher is teaching")


# class Mentor(Student, Teacher):
#     def guide(self):
#         print("Mentor is guiding students")


# # Creating object
# m = Mentor()

# # Calling all methods
# m.display_name()
# m.study()
# m.teach()
# m.guide()