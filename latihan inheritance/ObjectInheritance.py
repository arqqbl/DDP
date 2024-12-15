from latihanInheritance2 import *
from latihanInheritance3 import *

m1 = Mahasiswa("Siti Aminah","Wanita",20,"SI",3)
m2 = Mahasiswa("Budi Santoso","Pria",23,"TI",5)
d1 = Dosen("Sirojul Munir","Pria","44","S.Si, M.Kom","LPPM")
d2 = Dosen("Henry Saptono","Pria",44,"S.Si, M.Kom","LTSI")

d1.SetGaji(12000000)
d2.SetGaji(10000000)

m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()