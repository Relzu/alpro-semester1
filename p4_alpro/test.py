tarif : int = 200000
biaya_loker : int = 0

print("=== Sistem Pendaftaran Member Gym ===")
umur = int(input("Masukkan umur Anda: "))
if umur >= 15:
    kelas = input("Masukkan kelas Anda (yoga/boxing/zumba): ")
    if kelas == "yoga":
        print("Kelas Yoga")
        tarif = 300000
    elif kelas == "boxing":
        print("Kelas Boxing")
        tarif = 400000
    elif kelas == "zumba":
        print("Kelas Zumba")
        tarif = 250000
    else:
        print("Kelas Reguler")

    loker = input("Apakah Anda ingin menyewa loker? (ya/tidak): ")
    if loker == "ya":
        print("Loker telah ditambahkan")
        biaya_loker = 50000
    else:
        print("Tidak menyewa loker")

    print("\n=== Rincian Biaya ===")
    print("Kelas yang dipilih: ", kelas)
    print("Biaya Kelas: Rp.", tarif)
    print("Biaya Loker: Rp.", biaya_loker)
    print("------------------------------------")
    print("Total Biaya: Rp.", tarif + biaya_loker)
    
else:
    print("tidak cukup umur")