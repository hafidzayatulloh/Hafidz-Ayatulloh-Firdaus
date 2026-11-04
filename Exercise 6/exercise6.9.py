favorite_places = {
    'hafidz': ['Pantai Parangtritis', 'Gunung Lawu'],
    'sari': ['Gunung Lawu', 'Keraton Surakarta', 'Karimunjawa'],
    'andi': ['Bromo'],
}

for name, places in favorite_places.items():
    print(f"Tempat favorit {name.title()}:")
    for place in places:
        print(f"    {place}")
    print()