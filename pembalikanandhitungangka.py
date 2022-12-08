#nomor 1
kalimat = input("Masukan kata atau angka: ")
for i in range(len(kalimat), 0, -1):
    print(kalimat[i-1], end="")
#nomor 2
print("\n")
angka = input("Masukkan angka: ")
angka_hitung = input("Masukkan angka yang dihitung: ")

muncul = 0
for i in range(len(angka)):
    if angka[i] == angka_hitung:
        muncul += 1
        
print(f"angka {angka_hitung} muncul sebanyak {muncul} kali")