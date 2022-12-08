list_barang = {
    "susu": 20000,
    "permen": 500,
    "roti": 15000,
    "indomie": 3000,
    "vitamin": 50000
}

uang = int(input("Masukkan jumlah uang: "))
start = input("Ketik 'START' untuk mulai: ")
if(start.lower() != "start"):
    print("anda harus ketik 'START' untuk mulai")
else:
    while True:
        barang = input("apa barang yang akan anda beli ? ")
        barang = barang.lower()
        
        if(barang == "sudah"):
            break

        if((barang in list_barang) == False):
            print("Barang tidak tersedia")
        else:
            harga_barang = list_barang[barang]
            if(uang < harga_barang):
                print("Uang anda tidak cukup")
            else:
                uang -= list_barang[barang]
                print("Sisa uang anda : " + str(uang))