day = 4
match day: #untuk mencocokan
    case 1:
        print("Senin")
    case 2:
        print("Selasa")
    case 3:
        print("Rabu")
    case 4:
        print("Kamis")
    case 5:
        print("Jumat")
    case 6:
        print("Sabtu")
    case 7:
        print("Minggu")
    case 1 | 2 | 3 | 4 | 5 if month == 1:
        print("Liburan 67")
    case _: #kondisi default
        print("none")