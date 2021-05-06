#Membuat program biodata diri (menggunakan mode"w") = output berupa file.txt

print ("Program Biodata Diri")
print ("=================================")

# Mengambil input dari user
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")
jenis_kelamin = input("Jenis kelamin: ")

# format teks
teks = "Nama: {}\nUmur: {}\nAlamat: {}\nJenis kelamin: {}".format(nama, umur, alamat, jenis_kelamin)

# buka file untuk ditulis
file_bio = open("biodata.txt", "w")

# tulis teks ke file
file_bio.write(teks)

# tutup file
file_bio.close()