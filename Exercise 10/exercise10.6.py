try:
    first = int(input("Masukkan angka pertama: "))
    second = int(input("Masukkan angka kedua: "))
except ValueError:
    print("Maaf, yang kamu masukkan bukan angka.")
else:
    print(f"Hasil penjumlahan: {first + second}")