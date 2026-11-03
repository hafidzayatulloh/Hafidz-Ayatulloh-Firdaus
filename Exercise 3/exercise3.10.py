# Membuat list gunung-gunung di Indonesia
gunung = ['Rinjani', 'Semeru', 'Merapi', 'Bromo', 'Kerinci']

print("=== 1. List asli ===")
print(gunung)

# 2. Akses elemen dengan indeks
print("\n=== 2. Akses elemen (indeks) ===")
print(f"Gunung pertama: {gunung[0]}")
print(f"Gunung terakhir: {gunung[-1]}")

# 3. Mengubah elemen list
print("\n=== 3. Mengubah elemen (gunung[1] = 'Slamet') ===")
gunung[1] = 'Slamet'
print(gunung)

# 4. append() — tambah di akhir
print("\n=== 4. append('Sumbing') ===")
gunung.append('Sumbing')
print(gunung)

# 5. insert() — tambah di posisi tertentu
print("\n=== 5. insert(0, 'Jayawijaya') ===")
gunung.insert(0, 'Jayawijaya')
print(gunung)

# 6. del — hapus berdasarkan indeks
print("\n=== 6. del gunung[1] ===")
del gunung[1]
print(gunung)

# 7. pop() — hapus & ambil elemen terakhir
print("\n=== 7. pop() ===")
terakhir = gunung.pop()
print(f"Gunung yang di-pop: {terakhir}")
print(f"List setelah pop: {gunung}")

# 8. pop(indeks) — hapus & ambil elemen tertentu
print("\n=== 8. pop(0) ===")
pertama = gunung.pop(0)
print(f"Gunung yang di-pop: {pertama}")
print(f"List setelah pop: {gunung}")

# 9. remove() — hapus berdasarkan nilai
print("\n=== 9. remove('Merapi') ===")
gunung.remove('Merapi')
print(gunung)

# 10. len() — hitung jumlah elemen
print("\n=== 10. len() ===")
print(f"Jumlah gunung dalam list: {len(gunung)}")

# 11. sorted() — urut sementara (list asli tidak berubah)
print("\n=== 11. sorted() ===")
print(f"Urut alfabet (sementara): {sorted(gunung)}")
print(f"List asli tetap: {gunung}")

# 12. sorted(reverse=True) — urut terbalik sementara
print("\n=== 12. sorted(reverse=True) ===")
print(f"Urut alfabet terbalik (sementara): {sorted(gunung, reverse=True)}")
print(f"List asli tetap: {gunung}")

# 13. reverse() — balik urutan permanen
print("\n=== 13. reverse() ===")
gunung.reverse()
print(f"Setelah reverse(): {gunung}")

# 14. sort() — urut alfabet permanen
print("\n=== 14. sort() ===")
gunung.sort()
print(f"Setelah sort(): {gunung}")

# 15. sort(reverse=True) — urut alfabet terbalik permanen
print("\n=== 15. sort(reverse=True) ===")
gunung.sort(reverse=True)
print(f"Setelah sort(reverse=True): {gunung}")

# 16. index() — cari posisi suatu nilai
print("\n=== 16. index() ===")
print(f"Posisi 'Bromo': {gunung.index('Bromo')}")

# 17. count() — hitung kemunculan suatu nilai
print("\n=== 17. count() ===")
print(f"Jumlah 'Bromo' dalam list: {gunung.count('Bromo')}")

# 18. in — cek keberadaan elemen
print("\n=== 18. Operator 'in' ===")
print(f"Apakah 'Rinjani' ada? {'Rinjani' in gunung}")
print(f"Apakah 'Fuji' ada? {'Fuji' in gunung}")

# 19. len() pada list kosong
print("\n=== 19. List kosong ===")
gunung_kosong = []
print(f"List kosong: {gunung_kosong}")
print(f"Panjang list kosong: {len(gunung_kosong)}")