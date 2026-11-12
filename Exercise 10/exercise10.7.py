print("Kalkulator penjumlahan (ketik 'q' untuk keluar)")

while True:
    first = input("\nAngka pertama: ")
    if first == 'q':
        break

    second = input("Angka kedua: ")
    if second == 'q':
        break

    try:
        total = int(first) + int(second)
    except ValueError:
        print("Maaf, yang kamu masukkan bukan angka.")
    else:
        print(f"Hasil penjumlahan: {total}")