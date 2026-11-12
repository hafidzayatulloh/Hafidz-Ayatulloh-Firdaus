from pathlib import Path

names = []

while True:
    name = input("Masukkan namamu (ketik 'q' untuk selesai): ")
    if name == 'q':
        break

    names.append(name)
    print(f"Halo, {name}! Namamu sudah dicatat.")

contents = "\n".join(names) + "\n"

path = Path(__file__).parent / 'guest_book.txt'
path.write_text(contents, encoding='utf-8')