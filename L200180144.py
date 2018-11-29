#/usr/bin/python
#Menulis Data ke Dalam Berkas

#Kegiatan 1 dan 2
berkas = open("L200180144.txt" , "w")
berkas.write("L200180144\n")
berkas.write("Tl = 03-09-2000\n")
berkas.write("Nama = Vintan Kirana")
berkas.write("Kota Kelahiran = Sukoharjo")
berkas.close()
z = open ("L200180144.txt","r")
NIM = z.readline()
Tl = z.readline()
Nama = z.readline()
KotaKelahiran = z.readline()
print Nama
print KotaKelahiran, Tl
print NIM

#Kegiatan 3
import shelve
a = open ("L200180144.txt","r")
NIM = a.readline()
Tl = a.readline()
Nama = a.readline()
a.close()
a = shelve.open("vintan")
a['b'] = [NIM, Tl, Nama]
a.close()

#Kegiatan 4
a = shelve.open("vintan")
print a ['b']
print a ['b'][0]
print a ['b'][1]
print a ['b'][2]
