# Membuat class Manusia Sebagai Parent

class Manusia:
    def _init_(self, nama_depan, nama_belakang):
        self.firstname = nama_depan
        self.lastname = nama_belakang

    def printname(self):
        print("Nama saya " + self.firstname, self.lastname)


data = Manusia("Ruly", "Adhitya")
data.printname()