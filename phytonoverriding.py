# class Animal:

#     # attributes and method of the parent class
#     name = ""
    
#     def eat(self):
#         print("I can eat")

# # inherit from Animal
# class Dog(Animal):

#     # override eat() method
#     def eat(self):
#         print("I like to eat bones")

# # create an object of the subclass
# labrador = Dog()

# # call the eat() method on the labrador object
# labrador.eat()
class Laptop:

    tipe = ""
    
    def spesifikasi(self):
        print("Laptop ini memiliki spesifikasi dasar.")

class LaptopGaming(Laptop):

    def spesifikasi(self):
        print("Laptop ini memiliki spesifikasi tinggi untuk gaming, termasuk GPU dan RAM besar.")
        super().spesifikasi()

asus_gaming = LaptopGaming()

asus_gaming.spesifikasi()
