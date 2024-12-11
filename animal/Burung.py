from Animal import *
class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, suara):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna = suara

    def cetak_burung(self):
        super().cetak()
        print("Jenis \t\t\t:", self.jenis,"\n", 
            "suara \t\t\t:", self.warna)

lovebird = Burung("lovebird","Belatung","Udara","Bertelur","Lovebird Misty","kiwkiw")
lovebird.cetak_burung()
print("=====================================================================================")
murai = Burung("Murai","Biji bijian","Udara","Bertelur","Kucica Hutan","citcitcit")
murai.cetak_burung()