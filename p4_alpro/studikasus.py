#Farel Fadilah Hafizd
#267006111142
#Kelas G

print("=== Sistem Layanan Bengkel Motor===")
motor = int(input("Masukan tahun keluaran motor: "))
if motor >= 2010:
    print("\nPilihan servis: full/ringan")
    servis = input("masukan paket servis: ")
    if servis == "full":
        paket = "Servis Full"
        biaya_servis = 150000
    elif servis == "ringan":
        paket = "Servis Ringan"
        biaya_servis = 75000
    else:
        biaya_servis = 35000
        paket = "Reguler"
    oli = input("sekalian ganti oli? (y/t) ")
    if oli == "y":
        biaya_oli = 50000
    else:
        biaya_oli = 0

    print("\n=== Struk Bengkel ===")
    print("Tahun Motor: ", motor)
    print("Paket Servis: ", paket)
    print("Biaya Servis: ", biaya_servis)
    print("Biaya Oli: ", biaya_oli)
    print("----------------- +")
    tagihan = biaya_oli + biaya_servis
    print("Total Tagihan: ", tagihan)

    print("\n=== Proses Pembayaran ===")
    uang = int(input("Masukan nominal uang: "))
    if uang >= tagihan :
        total = uang - tagihan
        status = "TRANSAKSI BERHASIL"
        print ("Status: ",status)
        print ("Kembalian", total)
        print("Motor siap dibawa!")
    else:
        total = tagihan - uang
        status = "GAGAL"
        print("Status: ", status)
        print("Kurang: ", total)
        print("Motor belum bisa biambil")
else:
    print("Maaf kami tidak menerima motor keluaran dibawah 2010")
