print("Data nilai Mahasiswa BPD")
print("="*30)
nama=input("Nama : ")
fakultas=input("Fakultas : ")
matkul=input("Mata Kuliah : ")
tugas=float(input("Nilai Tugas : "))
uts=float(input("Nilai UTS : "))
uas=float(input("Nilai UAS : "))
print("="*30)
bobot_tugas = 0.30
bobot_uts = 0.30
bobot_uas = 0.40
nilai_akhir = (tugas * bobot_tugas) + (uts * bobot_uts) + (uas * bobot_uas)
print("Nilai Akhir : ", nilai_akhir)