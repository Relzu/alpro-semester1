#Farel Fadilah Hafizd
#267006111142
#Dinamis

nama = str(input("Masukkan Nama : "))
npm = int(input("Masukkan NPM : "))
kelas = str(input("Masukkan Kelas : "))
status = bool(input("Apakah Mahasiswa Aktif? (Ya/Tidak) : ")) == "True"
nilai : char 
konfirmasi : str

print("===Hasil Output===")
print(f"Nama : {nama} \nNPM : {npm} \nKelas : {kelas}")

if status == True:
    konfirmasi = "Mahasiswa Aktif"
else:
    konfirmasi = "Bukan Mahasiswa Aktif"

input_nilai = float(input("Masukkan Nilai : "))
if input_nilai > 80.0 and input_nilai <= 100.0:
    nilai = "A"
else:
    nilai = "Silahkan konfirmasi ke dosen pembimbing akademik anda untuk mengetahui nilai anda"

print(f"Nilai {nama}: {nilai} \nStatus Mahasiswa Aktif: {konfirmasi}")
print(type(nama), type(npm), type(kelas), type(nilai),type(status), type(konfirmasi))

#statis didefinisikan di awal, sedangkan dinamis didefinisikan saat runtime.