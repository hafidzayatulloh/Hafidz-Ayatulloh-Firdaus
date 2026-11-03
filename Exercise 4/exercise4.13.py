menu = ("nasi goreng", "soto ayam", "gado-gado", "sate ayam", "bakso")

print("Menu prasmanan:")
for food in menu:
    print(food)

print("\nMencoba mengubah item pertama...")
try:
    menu[0] = "mie goreng"
except TypeError as error:
    print(f"Python menolak perubahan: {error}")

menu = ("nasi goreng", "soto ayam", "rawon", "sate ayam", "pecel")

print("\nMenu yang sudah direvisi:")
for food in menu:
    print(food)
