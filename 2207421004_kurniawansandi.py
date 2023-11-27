class Toyota :
    def __init__(self, merek, harga):
        self.merek = merek
        self.harga = harga

Avanza = Toyota("1. Avanza 1.5 G CVT TSS","Rp.295.800.000")
Fortuner = Toyota("2. Fortuner 2.8 VRZ GR (4x4)","Rp. 302.500.000")
Supra = Toyota("3. SUPRA 3.0L A/T","Rp. 2.051.000.000")
Raize = Toyota("4. Raize 1.0 GR CVT TSS","Rp. 302.500.000")

print(Avanza.merek)
print(Avanza.harga)
print(Fortuner.merek)
print(Fortuner.harga)
print(Supra.merek)
print(Supra.harga)
print(Raize.merek)
print(Raize.harga)

Pilihan = input("Masukan Pilihan Anda :")

user_input = ''

while True:
    user_input = input('Tentukan Pilihan Anda ? yes/no: ')

    if user_input.lower() == 'yes':
        print('Silahkan Lanjutkan Tahap Berikutnya')
        break
    elif user_input.lower() == 'no':
        print('Terima Kasih')
        exit
    else:
        print('Type yes/no')

nama = input("Masukan Nama Anda : ")
alamat = input("Masukan Alamat Anda : ")
ktp = input("No KTP : ")
kk = input("NO KK(KARTU KELUARGA) : ")
npwp = input("NO NPWP : ")
rekening = input("Rekening Tabungan 3 bln terakhir : ")
slip = input("slip gaji bila bekerja/SKU bil : ")

user_input = input('Apakah Anda tertarik (yes/no): ')

if user_input.lower() == 'yes':
    print('user masukan yes')
    print('Tipe Perorangan')
    print("Berhasil")
elif user_input.lower() == 'no':
    print('user masukan no')
    print('Tipe Perorang')
    print("Gagal")
else:
    print('Type yes or no')
