print("""
Opsi:
# Aritmatika Dasar
	1. Penjumlahan
	2. Pengurangan
	3. Perkalian
	4. Pembagian
	5. Pembagian Bulat
	6. Modulus / Pembagian Habis
	7. Perpangkatan
	""")

opsi = int(input("Masukkan Opsi: "))

match opsi:
	case 1:
		print("#########-Aritmatika Penjumlahan-########")
		num_1 = float(input("masukkan angka ke 1: "))
		num_2 = float(input("masukkan angka ke 2: "))
		def func_penjumlahan(num_1, num_2):
			hasil = num_1+num_2
			print("hasil penjumlahan dari "+str(num_1)+" + "+str(num_2)+" adalah: "+str(hasil))
		func_penjumlahan(num_1, num_2)
	case 2:
		print("#########-Aritmatika Pengurangan-########")
		num_1 = float(input("masukkan angka ke 1: "))
		num_2 = float(input("masukkan angka ke 2: "))
		def func_pengurangan(num_1, num_2):
			hasil = num_1+num_2
			print("hasil pengurangan dari "+str(num_1)+" - "+str(num_2)+" adalah: "+str(hasil))
		func_pengurangan(num_1, num_2)
	case 3:
		print("#########-Aritmatika Perkalian-########")
		num_1 = float(input("masukkan angka ke 1: "))
		num_2 = float(input("masukkan angka ke 2: "))
		def func_perkalian(num_1, num_2):
			hasil = num_1*num_2
			print("hasil perkalian dari "+str(num_1)+" * "+str(num_2)+" adalah: "+str(hasil))
		func_perkalian(num_1, num_2)
	case 4:
		print("#########-Aritmatika Pembagian-########")
		num_1 = float(input("masukkan angka ke 1: "))
		num_2 = float(input("masukkan angka ke 2: "))
		def func_pembagian(num_1, num_2):
			hasil = num_1/num_2
			print("hasil pembagian dari "+str(num_1)+" / "+str(num_2)+" adalah: "+str(hasil))
		func_pembagian(num_1, num_2)
	case 5:
		print("#########-Aritmatika Pembagian Bulat-########")
		num_1 = float(input("masukkan angka ke 1: "))
		num_2 = float(input("masukkan angka ke 2: "))
		def func_pembagianBulat(num_1, num_2):
			hasil = num_1+num_2
			print("hasil pembagian bulat dari "+str(num_1)+" // "+str(num_2)+" adalah: "+str(hasil))
		func_pembagianBulat(num_1, num_2)
	case 6:
		print("#########-Aritmatika Modulus / Pembagian Habis-########")
		num_1 = float(input("masukkan angka ke 1: "))
		num_2 = float(input("masukkan angka ke 2: "))
		def func_modulus(num_1, num_2):
			hasil = num_1%num_2
			print("hasil modulus dari "+str(num_1)+" % "+str(num_2)+" adalah: "+str(hasil))
		func_modulus(num_1, num_2)
	case 7:
		print("#########-Aritmatika Perpangkatan-########")
		num_1 = float(input("masukkan angka ke 1: "))
		num_2 = float(input("masukkan angka ke 2: "))
		def func_perpangkatan(num_1, num_2):
			hasil = num_1**num_2
			print("hasil perpangkatan dari "+str(num_1)+" ^ "+str(num_2)+" adalah: "+str(hasil))
		func_perpangkatan(num_1, num_2)
	case _:
		print("\nmaaf opsi nomor "+str(opsi)+" tidak tersedia")