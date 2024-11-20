# # Nomer 1
# def celcius_ke_fahrenheit(celcius):
#     print((celcius * 9/5) + 32)
# celcius_ke_fahrenheit(100)
print("\n--- Megkonversi dari celcius ke fahrenheit---")
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit
print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))
    
print("\n--- Menentukan Bilangan Genap---")
# Nomer2
def is_genap(bilangan):
    return bilangan %2 ==0
print(is_genap(4))
print(is_genap(7))

print("\n---Mencari nilai kelulusan---")
# Nomer3
def nilai_kelulusan(nilai):
    if nilai >= 70:
        return "lulus"
    else :
        return "gagal"
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))


# Nomer4
print("\n--- Menampilkan bilangan ganjil---")

def ganjil(bilangan):
    for i in range(1, bilangan, 2):
        print(i, end=" ")
ganjil(20)


