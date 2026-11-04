rivers = {
    'nil': 'mesir',
    'amazon': 'brasil',
    'mississippi': 'amerika serikat',
}

for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui {country.title()}.")

print("\nSungai dalam dictionary:")
for river in rivers.keys():
    print(river.title())

print("\nNegara dalam dictionary:")
for country in rivers.values():
    print(country.title())