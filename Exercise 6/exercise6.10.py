favorite_numbers = {
    'hafidz': [7, 21],
    'sari': [3, 14, 99],
    'andi': [5],
    'dewi': [8, 12],
    'rina': [9, 18, 27],
}

for name, numbers in favorite_numbers.items():
    print(f"Angka favorit {name.title()}:")
    for number in numbers:
        print(f"    {number}")
    print()