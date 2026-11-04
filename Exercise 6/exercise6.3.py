glossary = {
    'variable': 'nama yang dipakai untuk menyimpan sebuah nilai.',
    'string': 'rangkaian karakter yang ditulis di antara tanda kutip.',
    'list': 'kumpulan item berurutan yang bisa diubah.',
    'tuple': 'kumpulan item berurutan yang tidak bisa diubah.',
    'dictionary': 'kumpulan pasangan key dan value.',
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n    {meaning}\n")