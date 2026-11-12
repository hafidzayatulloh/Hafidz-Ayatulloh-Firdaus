from pathlib import Path

path = Path(__file__).parent / 'learning_python.txt'

contents = path.read_text(encoding='utf-8')
print("Membaca seluruh file:")
print(contents.rstrip())

lines = contents.splitlines()

print("\nMembaca baris demi baris:")
for line in lines:
    print(line)