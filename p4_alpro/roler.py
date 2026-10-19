#Farel Fadilah Hafizd
#267006111142
#Kelas G

print("=== Pengecekan Tiket Roller Coaster ===")

umur = int(input("Masukkan umur Anda: "))
tinggi = int(input("Masukkan tinggi badan Anda (cm): "))
harga = 50000

if umur >= 12:
    if tinggi >= 150:
        print("Selamat! Anda dapat naik roller coaster")
        member = input("Apakah Anda member? (ya/tidak): ")
        if member == "ya":
            harga -= 10000
            print("Selamat! Anda mendapatkan diskon 10.000")

        print("Harga tiket roller coaster: Rp.", harga)
        uang = int(input("Masukkan jumlah uang yang ingin dibayar: "))

        if uang == harga:
            print("Uang pas")
        elif uang > harga:
            print("Kembalian: Rp.", uang - harga)
        else:
            print("Uang kurang: Rp.", harga - uang)
    else:
        print("u're short af")
else:
    print("Maaf, Anda tidak cukup umur untuk naik roller coaster")