sandwich_orders = ['tuna', 'ayam', 'telur', 'keju']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Saya sudah membuat sandwich {current_sandwich} pesananmu.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(sandwich.title())