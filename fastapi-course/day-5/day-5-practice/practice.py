# # Q1. Class and Object

# # Student naam ki class banao. Constructor mein name, age aur course accept karo. display_details() method se details print karo. Do student objects create karo.

# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def display_details(self):
#         print("name = ", self.name)
#         print("age = ", self.age)
#         print("course = ", self.course)
#         print("-----------------------------")


# std1 = Student("Sahil", 25, "Ai-Engineer")
# std2 = Student("vikash", 26, "Data-Engineer")

# std1.display_details()
# std2.display_details()
        



# # Q2. Constructor and self

# # Car class banao jisme brand, model aur price attributes hon. show_details() method se details print karo. Kam se kam 3 car objects create karo.

# class Car:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def show_details(self):
#         print("Car brand = ", self.brand)
#         print("Car model = ", self.model)
#         print("Car price = ", self.price)
#         print("------------------------")


# car1 = Car("Maruti", "Swift", 620000)
# car2 = Car("Hundai", "Creta", 1050000)
# car3 = Car("Toyota", "Fortuner", 5000000)

# car1.show_details()
# car2.show_details()
# car3.show_details()





# # Q3. Inheritance

# # Person naam ki parent class banao jisme name aur age hon. Student class usse inherit kare aur course attribute add kare. super() use karo.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_details(self):
#         print("Name = ", self.name)
#         print("Age = ", self.age)
#         print("-----------------------")

# class Student(Person):
#         def __init__(self, name, age, course):
#              super().__init__(name, age)
#              self.course = course

#         def display_course(self):
#             print("Name = ", self.name)
#             print("Age = ", self.age)
#             print("Course = ", self.course)
#             print("-----------------------")

# sd1 = Student("Abhinav", 29, "Backend + Cloud")

# sd1.display_details()
# sd1.display_course()




# # Q4. Encapsulation

# # BankAccount class banao. _balance attribute rakho. deposit(amount), withdraw(amount) aur get_balance() methods banao. Negative deposit aur insufficient balance handle karo.


# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self._balance = balance

#     def get_balance(self):
#         print("Name = ", self.name)
#         print("Balance = ", self._balance)
#         # return self._balance

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance = self._balance + amount
#             print("Amount deposit successfully !!")
#             print("Balance = ", self._balance)
#             print("----------------------------------")

#         else:
#             print("Please enter a valid number")
#             print("----------------------------------")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Please enter a valid amount!")

#         elif amount > self._balance:
#             print("Insufficient balance!")

#         else:
#             self._balance = self._balance - amount
#             print("Amount withdrawn successfully!")
#             print("Balance =", self._balance)

#         print("----------------------------------")

# ac1 = BankAccount("sahil", 50000)
# ac1.get_balance()
# ac1.deposit(2000)
# ac1.withdraw(500)
# ac1.get_balance()
          




# # Q5. Polymorphism

# # Animal parent class banao jisme sound() method ho. Dog aur Cat child classes mein sound() override karo. Teeno objects par same method call karo.

class Animal:
    def sound(slef):
        print("animal sounds ")
        print("--------------------------")

class Dog(Animal):
    def sound(self):
        print("Dog song is bark!!!")
        print("--------------------------")

class Cat(Animal):
    def sound(self):
        print('Cat sound is meawwwooooooo')
        print("--------------------------")

sound = Animal()
anm2 = Dog()
anm3 = Cat()

sound.sound()
anm2.sound()
anm3.sound()