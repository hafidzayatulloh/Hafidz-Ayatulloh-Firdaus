pizzas = ["pepperoni", "margherita", "BBQ chicken"]

# Salin list dengan slice
friend_pizzas = pizzas[:]

# Tambahkan pizza berbeda ke masing-masing list
pizzas.append("four cheese")
friend_pizzas.append("hawaiian")

print("Pizza favorit saya adalah:")
for pizza in pizzas:
    print(pizza)

print("\nPizza favorit teman saya adalah:")
for pizza in friend_pizzas:
    print(pizza)