class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    def cetak(self):
        print("Nama \t\t\t: ", self.nama,"\n",
              "makanan \t\t: ", self.makanan, "\n",
              "hidup \t\t\t: ", self.hidup,"\n",
              "berkembang biak \t: ", self.berkembang_biak)

# object1 = Animal("buaya", "daging", "air dan darat", "bertelur")
# object1.cetak()

