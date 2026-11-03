# Daftar tamu awal
tamu = ['Albert Einstein', 'Hafidz', 'Firdaus']

# Undangan pertama untuk semua tamu
print(f"Kepada {tamu[0]}, saya dengan hormat mengundang Anda untuk makan malam bersama.")
print(f"Kepada {tamu[1]}, saya dengan hormat mengundang Anda untuk makan malam bersama.")
print(f"Kepada {tamu[2]}, saya dengan hormat mengundang Anda untuk makan malam bersama.")

# Kabar: ada tamu yang tidak bisa hadir
print(f"\nKabar buruk: {tamu[1]} tidak bisa hadir di acara makan malam.")
print("=" * 50)

# Mengganti tamu yang tidak bisa hadir
tamu[1] = 'Ayatulloh'

# Undangan kedua untuk tamu yang masih tersisa
print(f"Kepada {tamu[0]}, saya dengan hormat mengundang Anda untuk makan malam bersama.")
print(f"Kepada {tamu[1]}, saya dengan hormat mengundang Anda untuk makan malam bersama.")
print(f"Kepada {tamu[2]}, saya dengan hormat mengundang Anda untuk makan malam bersama.")