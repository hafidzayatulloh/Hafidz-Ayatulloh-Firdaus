glossary = {
    'variable': 'nama yang dipakai untuk menyimpan sebuah nilai.',
    'string': 'rangkaian karakter yang ditulis di antara tanda kutip.',
    'list': 'kumpulan item berurutan yang bisa diubah.',
    'tuple': 'kumpulan item berurutan yang tidak bisa diubah.',
    'dictionary': 'kumpulan pasangan key dan value.',
    'loop': 'perintah yang mengulang sekumpulan kode.',
    'boolean': 'nilai yang hanya bisa True atau False.',
    'slice': 'bagian dari sebuah list.',
    'index': 'nomor posisi sebuah item di dalam list.',
    'comment': 'catatan di dalam kode yang diawali tanda pagar.',
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n    {meaning}\n")