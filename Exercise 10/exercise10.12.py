from pathlib import Path
import json

path = Path(__file__).parent / 'favorite_number.json'

if path.exists():
    contents = path.read_text(encoding='utf-8')
    number = json.loads(contents)
    print(f"Aku tahu angka favoritmu! Angkanya {number}.")
else:
    number = input("Berapa angka favoritmu? ")
    contents = json.dumps(number)
    path.write_text(contents, encoding='utf-8')
    print("Terima kasih! Angka favoritmu sudah kuingat.")