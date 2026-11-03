tempat = ['Jepang', 'Italia', 'Mesir', 'Brasil', 'Kanada']

print("=== Akses normal ===")
print(f"Tempat pertama: {tempat[0]}")
print(f"Tempat terakhir: {tempat[4]}")

#print("\n=== Mencoba akses indeks 5 (ERROR!) ===")
#print(tempat[5])   # IndexError: list index out of range

print("\n=== Setelah diperbaiki ===")
print(tempat[4])   # 'Kanada'