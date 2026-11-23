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
