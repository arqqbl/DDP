from latihanInheritance import *
class Dosen(Person):
    gelar = ""
    jabatan = ""

    def __init__(self, nama, gender, umur, gelar, jabatan):
        super().__init__(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan
    def SetGaji(self,uang):
        self.gaji = uang
    def cetak(self):
        super().cetak()
        print("Gelar \t\t:", self.gelar,
              "\nJabatan\t\t:", self.jabatan,
              "\nGaji\t\t:", self.gaji,
              "\n-------------------------------")
        