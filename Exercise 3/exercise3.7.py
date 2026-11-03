# Daftar tamu dari latihan 3-6 (6 orang)
tamu = ['Budi', 'Albert Einstein', 'Hartono', 'Hafidz', 'Firdaus', 'Sujatmiko']

# Kabar buruk: meja baru tidak datang tepat waktu
print("Kabar buruk! Meja makan baru tidak datang tepat waktu, jadi saya hanya bisa mengundang dua orang untuk makan malam.\n")

# Hapus tamu satu per satu dengan pop() sampai tersisa 2 orang
nama = tamu.pop()
print(f"Maaf {nama}, saya tidak bisa mengundang Anda ke makan malam.")

nama = tamu.pop()
print(f"Maaf {nama}, saya tidak bisa mengundang Anda ke makan malam.")

nama = tamu.pop()
print(f"Maaf {nama}, saya tidak bisa mengundang Anda ke makan malam.")

nama = tamu.pop()
print(f"Maaf {nama}, saya tidak bisa mengundang Anda ke makan malam.")

print("=" * 50)

# Undangan untuk 2 tamu yang masih tersisa
for orang in tamu:
    print(f"Kepada {orang}, Anda masih tetap diundang untuk makan malam bersama.")

print("=" * 50)

# Kosongkan list dengan del
del tamu[0]
del tamu[0]

# Pastikan list sudah kosong
print(f"Daftar tamu sekarang: {tamu}")