from random import sample

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
my_ticket = [3, 7, 'b', 10]

attempts = 0

while True:
    attempts += 1
    winning_ticket = sample(items, 4)

    if set(winning_ticket) == set(my_ticket):
        break

print(f"Tiket pemenang: {winning_ticket}")
print(f"Tiketmu: {my_ticket}")
print(f"Butuh {attempts} kali undian sampai tiketmu menang.")