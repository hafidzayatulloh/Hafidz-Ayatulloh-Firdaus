# Daftar tempat yang ingin dikunjungi (tidak urut alfabet)
tempat = ['Dieng', 'Bromo', 'Lombok', 'Bali', 'Mandalika']

# 1. Tampilkan list dalam urutan asli
print("Urutan asli:")
print(tempat)

# 2. Tampilkan urutan alfabet dengan sorted() TANPA mengubah list asli
print("\nUrutan alfabet (sorted, list asli tidak berubah):")
print(sorted(tempat))

# 3. Buktikan list masih dalam urutan asli
print("\nList masih urutan asli:")
print(tempat)

# 4. Tampilkan urutan alfabet terbalik dengan sorted(reverse=True)
print("\nUrutan alfabet terbalik (sorted reverse=True):")
print(sorted(tempat, reverse=True))

# 5. Buktikan list masih dalam urutan asli
print("\nList masih urutan asli:")
print(tempat)

# 6. Balik urutan list dengan reverse()
tempat.reverse()
print("\nSetelah reverse() — urutan berubah:")
print(tempat)

# 7. Balik lagi dengan reverse() — kembali ke urutan asli
tempat.reverse()
print("\nSetelah reverse() lagi — kembali ke urutan asli:")
print(tempat)

# 8. Urutkan permanen dengan sort() — alfabet
tempat.sort()
print("\nSetelah sort() — urutan alfabet permanen:")
print(tempat)

# 9. Urutkan permanen dengan sort(reverse=True) — alfabet terbalik
tempat.sort(reverse=True)
print("\nSetelah sort(reverse=True) — urutan alfabet terbalik permanen:")
print(tempat)