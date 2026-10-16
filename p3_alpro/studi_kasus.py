
print("=== Sistem Manajemen Muatan Ekspedisi ===")
supir =input("Nama Supir :")
kapasitas_maks = int(input("Kapasitas Maks Truk (Kg) : "))
rata2 = float(input("Berat: rata-rata per paket (Kg): "))
jumlah_muatan = int(input("Jumlah paket yang dimuat :" ))

total_berat = rata2 * jumlah_muatan
total_berat += 120
selisih = kapasitas_maks - total_berat

print("\n=== Ringkasan Muatan ===")
print("Supir Bertugas : ", supir)
print("Total Muatan: ", total_berat, "Kg")
print("Sisa Ruang Kapasitas: ", selisih , " Kg")

print("\n=== Status Kelayakan Jalan ===")
print("Apakah truk aman untuk berangkat?", total_berat <= kapasitas_maks)
print("Apakah truk overload?", total_berat > kapasitas_maks)
print("Apakah muatan truk pas maksimal?", total_berat == kapasitas_maks)
