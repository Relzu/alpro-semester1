nama : str
kelas : str = "Informatika G 26"

input_nama = input("Masukkan Nama : ")
if input_nama:
    nama = input_nama
    print(f"Nama : {nama} \nKelas : {kelas}")
    print("nama", type(nama), "kelas", type(kelas))