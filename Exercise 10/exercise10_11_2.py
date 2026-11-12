from pathlib import Path
import json

path = Path(__file__).parent / 'favorite_number.json'
contents = path.read_text(encoding='utf-8')
number = json.loads(contents)

print(f"Aku tahu angka favoritmu! Angkanya {number}.")