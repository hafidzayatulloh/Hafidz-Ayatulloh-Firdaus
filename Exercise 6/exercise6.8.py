pet_1 = {'kind': 'kucing', 'owner': 'Hafidz'}
pet_2 = {'kind': 'anjing', 'owner': 'Sari'}
pet_3 = {'kind': 'kelinci', 'owner': 'Andi'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print("Hewan peliharaan:")
    for key, value in pet.items():
        print(f"    {key.title()}: {value.title()}")
    print()