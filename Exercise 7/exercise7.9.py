sandwich_orders = [
    'tuna', 'pastrami', 'ayam', 'pastrami', 'telur', 'keju', 'pastrami'
]
finished_sandwiches = []

print("Maaf, pastrami sudah habis.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Saya sudah membuat sandwich {current_sandwich} pesananmu.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(sandwich.title())