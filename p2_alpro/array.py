#Farel Fadilah Hafizd
#267006111142

nama : list = ["Farel", "Febri", "Jawira"]
npm : list = ["267006111142", "267006111143", "267006111144"]

npm = input("Masukkan NPM : ")

for i in range(len(npm)):
    if int(npm[i]) % 2 == 0:
        print(f"Nama : {nama[i]} NPM : {npm[i]}")
