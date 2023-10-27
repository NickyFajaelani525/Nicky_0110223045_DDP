#deklarasi dan inisialisasi variabel
pelanggan ="Budi Santoso"
totalBelanja = 15000

#Struktur Kendali if
if(totalBelanja < 100000):
    Keterangan ="Selamat Anda Mendapatkan Hadiah"
else:
    Keterangan ="Terimakasih sudah berbelanja"

#cetak data 
print("Pelanggan",pelanggan, "\nTotal Belanja Anda Rp." ,totalBelanja, "\n" ,Keterangan )



cuaca = input ("apakah cuaca hari ini?")

match cuaca:
    case "panas"
    print "memakai sunscreen"
match 