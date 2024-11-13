class Laptop:
    def __init__(self, merk="", prosesor=""):
        self._merk = merk
        self._prosesor = prosesor
        print("Laptop dibuat.")

    def nyalakan(self):
        print("Laptop dinyalakan")

    # Getter untuk _merk
    def get_merk(self):
        return self._merk

    # Setter untuk _merk
    def set_merk(self, merk):
        self._merk = merk

    # Getter untuk _prosesor
    def get_prosesor(self):
        return self._prosesor

    # Setter untuk _prosesor
    def set_prosesor(self, prosesor):
        self._prosesor = prosesor

    def __del__(self):
        print("Laptop dihapus.")


class GamingLaptop(Laptop):
    def __init__(self, merk="", prosesor=""):
        super().__init__(merk, prosesor)
        print("Gaming Laptop dibuat.")

    def nyalakan(self):
        super().nyalakan()
        print(f"Laptop gaming merk {self.get_merk()} dengan prosesor {self.get_prosesor()} siap digunakan untuk bermain.")

    def __del__(self):
        print("Gaming Laptop dihapus.")
        super().__del__()


# Membuat objek dan menggunakan setter
laptop_gaming = GamingLaptop()
laptop_gaming.set_merk("ASUS ROG")  # menggunakan setter
laptop_gaming.set_prosesor("Intel i9")  # menggunakan setter
laptop_gaming.nyalakan()

del laptop_gaming
