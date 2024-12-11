from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("Design \t\t\t:", self.design,"\n", 
            "Racun \t\t\t:", self.racun)
    
anaconda = Ular("Anaconda", "Daging", "Darat", "Bertelur", "Batik akatsuki","Tidak beracun")
anaconda.cetak_ular()
print("=====================================================================================")
pyton = Ular("Pyton","Daging","Darat","Bertelur","Ungu janda","Beracun")
pyton.cetak_ular()
print("=====================================================================================")