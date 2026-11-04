prompt = "\nBerapa umurmu? (ketik 'quit' untuk selesai) "

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Tiket kamu gratis.")
    elif age <= 12:
        print("Harga tiket kamu $10.")
    else:
        print("Harga tiket kamu $15.")