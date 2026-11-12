from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(__file__).parent / filename

    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"\nMaaf, file {filename} tidak ditemukan.")
    else:
        print(f"\nIsi {filename}:")
        print(contents.rstrip())