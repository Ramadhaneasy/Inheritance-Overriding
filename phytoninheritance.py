# class Animal:

#     # attribute and method of the parent class
#     name = ""
    
#     def eat(self):
#         print("I can eat")

# # inherit from Animal
# class Dog(Animal):

#     # new method in subclass
#     def display(self):
#         # access name attribute of superclass using self
#         print("My name is ", self.name)

# # create an object of the subclass
# labrador = Dog()

# # access superclass attribute and method 
# labrador.name = "Rohu"
# labrador.eat()

# # call subclass method 
# labrador.display()
class Laptop:

    tipe = ""
    
    def spesifikasi(self):
        print("Laptop ini memiliki spesifikasi dasar.")

class LaptopGaming(Laptop):

    def layar(self):
        print("Laptop ini memiliki spesifikasi tinggi untuk gaming, termasuk GPU dan RAM besar.",self.tipe)

asus_gaming = LaptopGaming()

asus_gaming.tipe="GPU KENCANG"
asus_gaming.spesifikasi()

asus_gaming.layar()

