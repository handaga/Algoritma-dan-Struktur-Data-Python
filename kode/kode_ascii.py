
print("Tabel KODE ASSCII")
print("-----------------")
## Nilai variabel kode akan berubah secara otomatis mulai dari 32 sampai 126
for kode in range(32,126):
    print("%3c | %4d | %12s | %6s |" %( kode, kode, bin(kode), hex(kode) ) )
print("-----------------")

    

    
