cities = {
    'jakarta': {
        'country': 'Indonesia',
        'population': 10_500_000,
        'language': 'Indonesia',
        'fact': 'ibu kota Indonesia saat ini.',
    },
    'tokyo': {
        'country': 'Jepang',
        'population': 14_000_000,
        'language': 'Jepang',
        'fact': 'salah satu kota terbesar di dunia.',
    },
    'paris': {
        'country': 'Prancis',
        'population': 2_100_000,
        'language': 'Prancis',
        'fact': 'rumah bagi Menara Eiffel.',
    },
    'surakarta': {
        'country': 'Indonesia',
        'population': 520_000,
        'language': 'Indonesia dan Jawa',
        'fact': 'dikenal juga dengan nama Solo.',
    },
}

for city, info in cities.items():
    print(f"Kota: {city.title()}")
    print(f"    Negara: {info['country']}")
    print(f"    Populasi: sekitar {info['population']:,}")
    print(f"    Bahasa: {info['language']}")
    print(f"    Fakta: {info['fact']}\n")