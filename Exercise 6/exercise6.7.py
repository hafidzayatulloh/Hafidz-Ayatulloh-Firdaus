person_1 = {
    'first_name': 'Hafidz',
    'last_name': 'Firdaus',
    'age': 19,
    'city': 'Karangnyar',
}

person_2 = {
    'first_name': 'Sari',
    'last_name': 'Wulandari',
    'age': 22,
    'city': 'Surakarta',
}

person_3 = {
    'first_name': 'Andi',
    'last_name': 'Pratama',
    'age': 30,
    'city': 'Yogyakarta',
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Nama: {full_name}")
    print(f"Umur: {person['age']}")
    print(f"Kota: {person['city']}\n")