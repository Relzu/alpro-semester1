angka1 = int(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /, %, **, //): ")
angka2 = int(input("Masukkan angka kedua: "))

#dictionary tidak ada di laprak
hasil = {
    '+': angka1 + angka2,
    '-': angka1 - angka2,
    '*': angka1 * angka2,
    '/': angka1 / angka2,
    '%': angka1 % angka2,
    '**': angka1 ** angka2,
    '//': angka1 // angka2
}


print("Hasil:", hasil[operator])