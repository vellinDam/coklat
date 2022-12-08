def panggilyuk() :
    print("~~ Table Matematika Nich ~~")
    print("Pilihan Model Matematika")
    print("1. Perkalian")
    print("2. Pembagian")
    count   = (int(input("Masukan model matematika yang diinginkan 1/2 :")))
    if(count>2):
        print("Pilihan tidak tersedia jangan ngasal!")
        exit()
    count1 = (int(input("Menampilkan table matematika dari angka : ")))
    if(count==1):
        for i in range (1,11):
            print(count1,"x", i , "=" , count1*i)
    elif(count==2):
        for i in range (50,66):
             print(i,":", count1 , "=" , i/count1)
panggilyuk()