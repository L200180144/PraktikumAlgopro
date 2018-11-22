##Kegiatan 1. Membuat modul

a={'nim':'144','nama':'vintan','alamat':'sukoharjo','status':'mahasiswa','fakultas':'fki','hobi':'jalan-jalan','motto hidup':'terbentur terbentur terbentuk', 'keluar':'terimakasih'}
def nim():
    print 'nim',a['nim']
def nama():
    print 'nama',a['nama']
def alamat():
    print 'alamat',a['alamat']
def status():
    print 'status',a['status']
def fakultas():
    print 'fakultas',a['fakultas']
def hobi():
    print 'hobi',a['hobi']
def motto_hidup():
    print 'motto hidup',a['motto hidup']
def keluar () :
    print ' ',a['keluar']
def pilihan():
    print 'pilihan yang tersedia:'
    print 'b menampilkan bantuan ini'
    print 'N menampilkan nim'
    print 'a menampilkan nama'
    print 'i menampilkan alamat'
    print 't menampilkan status'
    print 'o menampilkan fakultas'
    print 'k menampilkan hobi'
    print 'u menampilkan motto hidup'
    print 'K menampilkan keluar'
pilihan()

g=str(raw_input('pilihan saudara:'))
while g != 'p':
    if g == 'a':
        nama()
        g=str(raw_input('pilihan saudara:'))
    elif g == 'b':
        pilihan()
        g=str(raw_input('pilihan saudara:'))
    elif g == 'N':
        nim()
        g=str(raw_input('pilihan saudara:'))
    elif g == 'i':
        alamat()
        g=str(raw_input('pilihan saudara:'))
    elif g == 't':
        status()
        g=str(raw_input('pilihan saudara:'))
    elif g == 'o':
        fakultas()
        g=str(raw_input('pilihan saudara:'))
    elif g == 'k':
        hobi()
        g=str(raw_input('pilihan saudara:'))
    elif g == 'u':
        motto_hidup()
        g=str(raw_input('pilihan saudara:'))
    elif g == 'K':
        keluar()
        g=str(raw_input('pilihan saudara:'))
