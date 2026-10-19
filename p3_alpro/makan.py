print ("===Kalkulator Patungan Makan===")

nama = input("Masukkan nama Anda: ")

tagihan1 = float(input("Total Tagihan (Rp): "))
persentip = int(input("Persentase tip/pajak (misal 67): "))
jumlah_orang = int(input("Jumlah orang yang ikut patungan: "))

nominal_tip = (persentip / 100) * tagihan1
total_tagihan = tagihan1 + nominal_tip
bayar_per_orang = total_tagihan / jumlah_orang

print("\n===Ringkasan Tagihan===")
print("Selamat datang," + nama + "!")
print("Total tagihan dan tip adalah: ", total_tagihan)
print("Setiap orang harus membayar: ", bayar_per_orang)