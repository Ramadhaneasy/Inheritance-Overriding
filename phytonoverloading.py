class A:
    # Overloading the + operator
    def __add__(self, other):
        return self.a + other.a

# Membuat objek dan menetapkan atribut langsung
ob1 = A()
ob1.a = 1

ob2 = A()
ob2.a = 2

ob3 = A()
ob3.a = "Geeks"

ob4 = A()
ob4.a = "For"

# Menggunakan operator + untuk penjumlahan
print(ob1 + ob2)   # Output: 3
print(ob3 + ob4)   # Output: GeeksFor

# Contoh pemanggilan langsung metode __add__
print(A.__add__(ob1, ob2))  # Output: 3
print(A.__add__(ob3, ob4))  # Output: GeeksFor

# Pemanggilan menggunakan objek
print(ob1.__add__(ob2))     # Output: 3
print(ob3.__add__(ob4))     # Output: GeeksFor
