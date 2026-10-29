#Farel Fadilah Hafizd
#267006111142
#Kelas G

print("=== Simulasi Rental PlayStation ===") 
 
jumlah_pelanggan = int(input("Masukkan jumlah pelanggan: ")) 
pelanggan_padam = int(input("Masukkan nomor pelanggan saat listrik padam (0 jika tidak ada): "))
 
tarif_per_jam = 10000 
pendapatan_rental = 0 
 
for pelanggan in range(1, jumlah_pelanggan + 1): 
    print("\n--- Melayani Pelanggan Ke-", pelanggan, "---") 
 
    if pelanggan == pelanggan_padam: 
        print("INFO: Listrik padam. Rental ditutup!") 
        break 
 
    total_sewa = 0 
 
    for jam in range(1, 4): 
        if jam == 2: 
            print("Jam ke-2 sudah dipesan orang lain. Jam dilewati.") 
            continue 
 
        print("Jam ke-", jam, ": tarif Rp", tarif_per_jam) 
        total_sewa += tarif_per_jam 
    else: 
        print("Status: Semua jam sewa Pelanggan", pelanggan, "telah diproses.") 
        print("Total pembayaran Pelanggan", pelanggan, ": Rp", total_sewa)
        pendapatan_rental += total_sewa 
 
print("\n=== Laporan Tutup Rental ===") 
print("Total pendapatan rental: Rp", pendapatan_rental) 