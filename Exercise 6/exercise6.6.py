favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people = ['jen', 'budi', 'edward', 'sari', 'phil']

for person in people:
    if person in favorite_languages:
        print(f"Terima kasih {person.title()} sudah mengisi polling!")
    else:
        print(f"{person.title()}, silakan ikut polling bahasa favorit!")