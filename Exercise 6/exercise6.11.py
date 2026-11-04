cities = {
    'jakarta': {
        'country': 'Indonesia',
        'population': 10_500_000,
        'fact': 'ibu kota Indonesia saat ini.',
    },
    'tokyo': {
        'country': 'Jepang',
        'population': 14_000_000,
        'fact': 'salah satu kota terbesar di dunia.',
    },
    'paris': {
        'country': 'Prancis',
        'population': 2_100_000,
        'fact': 'rumah bagi Menara Eiffel.',
    },
}

for city, info in cities.items():
    print(f"Kota: {city.title()}")
    print(f"    Negara: {info['country']}")
    print(f"    Populasi: sekitar {info['population']:,}")
    print(f"    Fakta: {info['fact']}\n")