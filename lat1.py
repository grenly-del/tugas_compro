#PESAN
print('Berikut ini adalah aplikasi Matematika')
print('Berikut Pilihan Operasi:')

print("1. Operasi Tambah ( + )")
print("2. Operasi Kurang ( - )")
print("3. Operasi Kali ( * )")
print("4. Operasi Bagi ( / )")
print("5. Operasi Pangkat ( ^ )")
print('6. Hitung fahrenheit')
print('7. Hitung Luas Persegi')

def proses(operasi):
	if 1 <= operasi <=4:
	#INPUT
		angka_1 = int(input('Masukkan angka pertama : '))
		angka_2 = int(input('Masukkan angka kedua : '))
		if operasi == 1:
			print(angka_1 + angka_2)
		elif operasi == 2:
			print(angka_1 - angka_2)
		elif operasi == 3:
			print(angka_1 * angka_2)
		elif operasi == 4:
			print(int(angka_1 / angka_2))
	elif operasi == 5:
		angka_3 = float(input('Masukkan angka yang ingin di pangkatkan! : '))
		angka_4 = float(input('Masukkan angka pangkatnya! : '))
		print(f"Hasilnya : {angka_3 ** angka_4}")
	elif operasi == 6:
		celcius = float(input('Masukkan Celcius : '))
		print(f"Suhu Dalam fahrenheit : {(celcius *9/5)+32}")
	elif operasi == 7:
		lebar = int(input('Masukkan lebar! : '))
		panjang = int(input('Masukkan panjang! : '))
		print(f"Luas perseginya adalah: {lebar*panjang}")
	else:
		print('Pilihan Tersebut Tidak Ada')

try:
	operasi = int(input('Pilih Operasi Nomor Berapa ? : '))
	proses(operasi)
except ValueError:
	print('Terjadi Error Dengan pilihan yang di pilih')



