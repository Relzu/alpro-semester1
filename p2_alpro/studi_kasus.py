nama = str(input("Masukkan Nama : "))
umur = int(input("Umur Pembeli : "))
tiket = int(input("Jumlah Tiket : "))
bayar = float(input("Uang Pembayaran : "))

film : str = "A Silent Voice"
genre : str = "Slice of Life"
tayang : bool = True
harga : float = 6767.67

print("===== INFORMASI / DATA BIOSKOP =====")
print(f"Nama Film: {film} \nGenre Film: {genre} \nFilm Sedang Tayang: {tayang} \nHarga Tiket: Rp {harga}")

print("\n===== DATA PEMBELI =====")
print(f"Nama: {nama} \nUmur: {umur} \nJumlah Tiket: {tiket} \nUang Pembayaran: Rp {bayar}")

print("\n===== TIPE DATA VARIABEL =====")
print(f"film: {type(film)} \ngenre: {type(genre)} \ntayang: {type(tayang)}\nharga: {type(harga)} \nnama: {type(nama)} \numur: {type(umur)} \ntiket: {type(tiket)} \nbayar: {type(bayar)}")