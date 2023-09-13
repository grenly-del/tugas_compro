const readline = require('readline')
const { stdin: input, stdout: output } = require('node:process');

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
})

rl.question(`1. Tambah ( + )
2. Kurang ( - )
3. Kali ( x )
4. Bagi ( : )
5. Hitung Luas Persegi
6. Hitung Fahrenheit

Silahkan pilih Operasi yang akan di gunakan : `, (data) => {
	if( data >= 1 && data <= 4) {
		console.log('Penjumlahan')
		 operasiPenjumlahan(data)
	}else if ( data == 5 ) {
		rl.question('Masukkan Lebar : ', (l) => {
			rl.question('Masukkan Tinggi : ', (t) => {
				console.log(`Luasnya adalah : ${l*t}`)
				rl.close()
			})
		})
	}else if( data == 6) {
		rl.question('Masukkan Celcius : ', (c) => {
			console.log(`Fahrenheit ${(c *9/5)+32}`)
			rl.close()
		})
	}else {
		rl.close()
	}
	
})



const operasiPenjumlahan = (data => {
	rl.question('Masukkan angka pertama : ', (c1) => {
		rl.question('Masukkan angka kedua : ', (c2) => {
			if( data == 1 || data == '+' ) {
				console.log(`Hasil Operasinya : ${c1+c2}`)
			}else if( data == 2 || data == '-' ) {
				console.log(`Hasil Operasinya : ${c1-c2}`)
			}else if (data == 3 || data == 'x') {
				console.log(`Hasil Operasinya : ${c1*c2}`)
			}else if (data == 4 || data == ':') {
				console.log(`Hasil Operasinya : ${c1/c2}`)
			}else{console.log('Maaf ada yang salah')}
			rl.close()
		})
	})
})