from pathlib import Path

path = Path(__file__).parent / 'learning_python.txt'

contents = path.read_text(encoding='utf-8')
print("Membaca seluruh file:")
print(contents.rstrip())

print("\nMembaca baris demi baris:")
for line in contents.splitlines():
    print(line)