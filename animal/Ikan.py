from Animal import *
class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna =warna

    def cetak_ikan(self):
        super().cetak()
        print("Jenis \t\t\t:", self.jenis,"\n", 
            "Warna \t\t\t:", self.warna)

hiu = Ikan("Hiu","Daging","Air Asin","Bertelur","Megalodon","Biru")
hiu.cetak_ikan()
print("=====================================================================================")
cupang = Ikan("Cupang","Pelet","Air Tawar","Bertelur","Slayer","Ijo Neon")
cupang.cetak_ikan()