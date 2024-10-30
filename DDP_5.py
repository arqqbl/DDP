pilihan = int (input ("masukan pilihan :"))
    
match pilihan :
        case 1 :
            print ("menghitung luas persegi")
            s = int (input("masukan sisi :"))
            LuasPersegi = s * s
            print (f"Luas persegi dengan sisi {s} adalah {LuasPersegi}")
        case 2 :
            print ("menghitung luas lingkaran")
            pi : 3.14
            r = int(input("masukan rusuk lingkaran"))
            LuasLingkaran = pi * r ** 2
            print (f"luas lingkaran dengan rusuk {r} adalah {LuasLingkaran}")
        case 3 :
            print ("menghitung luas segitiga")
            alas = int(input("masukan alas segitiga"))
            tinggi = int(input("masukan tinggi segitiga"))
            LuasSegitiga = 1/2 * alas * tinggi
            print (f"luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {LuasSegitiga}")
        case _:
            print ("input tidak valid")

