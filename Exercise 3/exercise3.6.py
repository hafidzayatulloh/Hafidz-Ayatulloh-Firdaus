# Daftar tamu dari latihan sebelumnya (3-5)
tamu = ['Albert Einstein', 'Hafidz', 'Firdaus']

# Kabar baik: meja makan lebih besar
print("Kabar baik! Saya menemukan meja makan yang lebih besar, jadi saya bisa mengundang lebih banyak tamu.\n")

# Tambah 1 tamu di awal list
tamu.insert(0, 'Budi')

# Tambah 1 tamu di tengah list
tamu.insert(2, 'Hartono')

# Tambah 1 tamu di akhir list
tamu.append('Sujatmiko')

# Undangan untuk semua tamu
for orang in tamu:
    print(f"Kepada {orang}, saya dengan hormat mengundang Anda untuk makan malam bersama.")