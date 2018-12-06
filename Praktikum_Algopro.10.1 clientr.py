#client
#praktikum 10 kegiatan 1

import socket
	
hostname = 'localhost'
pesan = ''
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50005))
print "Mesin penjawab otomatis sudah siap"
while pesan.lower() != 'keluar':
	pesan = raw_input('Perintah: ')
	s.send(pesan)
	if pesan.lower() != 'keluar':
            response = s.recv(1025)
            print 'Jawaban', response
	else:
            print 'siap'
            s.close()
