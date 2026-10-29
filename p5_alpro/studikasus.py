#Farel Fadilah Hafizd
#267006111142
#Kelas G

print("=== Simulasi Tabungan Liburan ===")
lama_menabung = int(input("Berapa minggu nabung? "))
berapa_uang = int(input("Uang yang ditabung setiap sesi: "))
total_uang = 0

print("\n=== Mulai Menabung ===")
for minggu in range (1, lama_menabung + 1):
    print("\nMinggu ke", minggu)
    for hari in range (1, 4):
        print("Hari ke", hari)
        if hari in (2,6):
            print("akew ogah nabung.")
            continue
        for sesi in range (1,3):
            print("-> Sesi",sesi, "- nabung: ", berapa_uang)
            total_uang += berapa_uang
else:
    print("\nMenabung selama",lama_menabung, "minggu - the goals is over, sana pemborosan.")

print("\n=== Hasil Tabungan ===")
if total_uang >= 200000:
    print("dana anda Rp", total_uang, "- hidup cuman sekali, ayo boros.")
elif total_uang >= 50000:
    print("dana Rp", total_uang, "- aduh gimana ya buat survive.")
else:
    print("dana anda Rp", total_uang, "- mas tau diri please jangan boros.")