bruh = ["67","68","69"]
for x in bruh:
    if x == "69":
        break
    if x == "67" :
        continue
    print(x)

n = int(input("Jumlah looping: "))
for i in range (0,n):
    print("67")
    
else:
    print("Wallahi I'm finished.")

#nested loop
#kasus 1
for baris in range (1,4):
    for kolom in range(1,3):
        print("Baris",baris, "- Kolom",kolom)
#nested loop
#kasus 2
for baris in range (1,4):
    print("\nbaris",baris)
    for kolom in range(1,3):
        print("kolom",kolom)
        for dimensi in range (1,5):
            print("dimensi",dimensi)