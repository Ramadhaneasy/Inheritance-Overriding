class A:
    # Konstruktor untuk menetapkan nilai awal atribut `a`
    def __init__(self, nilai=None):
        self._a = nilai
        print("Objek A dibuat.")

    # Overloading the + operator
    def __add__(self, other):
        return self._a + other._a

    # Setter untuk `a`
    def set_a(self, nilai):
        self._a = nilai

    # Getter untuk `a`
    def get_a(self):
        return self._a

    # Destruktor
    def __del__(self):
        print("Objek A dihapus.")


# Membuat objek dan menetapkan atribut melalui setter
ob1 = A()
ob1.set_a(1)

ob2 = A()
ob2.set_a(2)

ob3 = A()
ob3.set_a("Geeks")
ob4 = A()
ob4.set_a("For")

# Menggunakan operator + untuk penjumlahan
print(ob1 + ob2)   # Output: 3
print(ob3 + ob4)   # Output: GeeksFor

# Contoh pemanggilan langsung metode __add__
print(A.__add__(ob1, ob2))  # Output: 3
print(A.__add__(ob3, ob4))  # Output: GeeksFor

# Pemanggilan menggunakan objek
print(ob1.__add__(ob2))     # Output: 3
print(ob3.__add__(ob4))     # Output: GeeksFor

# Menggunakan getter untuk melihat nilai saat ini
print(ob1.get_a())          # Output: 1
print(ob3.get_a())          # Output: Geeks

# Menghapus objek
del ob1
del ob2
del ob3
del ob4
