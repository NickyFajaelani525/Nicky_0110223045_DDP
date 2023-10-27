#Siswa dinyatakan lulus minimal 60 nilainya 
nama = "Nicky Fajaelani"
matpel = "Matematika"
nilai = 88

#ternary
Keterangan = "lulus" if nilai >= 60 else "gagal"

#cetak data 
print("Nama Siswa \t:",nama,
      "\nMata Pelajaran \t:",matpel,
      "\nNilai \t\t:",nilai,
      "\nKeterangan \t:",Keterangan)




nama = "Nicky Fajaelani"
matpel = "mtk"
nilai = 88

#uji grade dengan IF Multi Kondisi
if(nilai >= 85 and nilai <= 100):
    grade = "A"
elif(nilai >= 75 and nilai <= 85):
    grade = "B"
elif(nilai >= 60 and nilai <= 75):
    grade = "C"
elif(nilai >= 30 and nilai <= 60):
    grade = "D"
else:
    grade ="E"

#cetak data
print("Nama Siswa \t:",nama,
      "\nMata Pelajaran \t:",matpel,
      "\nNilai \t\t:",nilai,
      "\nKeterangan \t:",grade)
