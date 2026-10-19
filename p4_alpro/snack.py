#Farel Fadilah Hafizd
#267006111142
#Kelas G

toko = input("Apakah toko buka: ")

if toko == "ya":
    print("Toko buka")
    makanan = input("Masukkan makanan yang ingin dibeli: ")
    harga = 0
    if makanan == "snack":
        harga = 20000
        print("Harga Snack: Rp", harga)
    elif makanan == "minuman":
        harga = 5000
        print("Harga Minuman: Rp", harga)
    else:
        print("Makanan tidak tersedia")

    uang = int(input("Masukkan jumlah uang yang ingin dibayar: "))
    if uang == harga:
        print("Uang pas")
    elif uang > harga:
        kembalian = uang - harga
        print("Kembalian: Rp", kembalian)
    else:
        kekurangan = harga - uang
        print("Uang kurang: Rp", kekurangan)
else:
    print("Toko tutup")