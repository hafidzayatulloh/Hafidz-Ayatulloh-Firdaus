prompt = "\nMasukkan topping pizza (ketik 'quit' untuk selesai): "
topping = ""

while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"Saya akan menambahkan {topping} ke pizzamu.")