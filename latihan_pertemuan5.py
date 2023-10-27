vehiclename = ["ZX-25R","motor sport", "250 cc", "hijau, roda dua"]
vehiclename.append("125 Juta")
vehiclename.append("standar")
vehiclename.insert(2,"Kawasaki")

print(vehiclename)

print("""
    *** Pilih Operasi ***
      1. Hitung Persegi
      2. Hitung Lingkaran
      3. Hitung Segitiga
    """)

pilihan = input("Masukan pilihan:")
match pilihan:
    case "1":
        s = int(input("masukkan sisi:"))
        persegi = s*s
        print("L = s x s.", persegi)
    case "2":
        phi = 3.14
        j = int(input("masukan jari:"))
        lingkaran =phi *j*j
        print("= π x r²", lingkaran)
    case "3":
        l = 1/2
        a = int(input("masukan alas:"))
        t = int(input("masukan tinggi:"))
        segitiga = l*a*t
        print("L = 1/2 x a x t", segitiga)
    case _:
        print("pilihan tidak tersedia")







