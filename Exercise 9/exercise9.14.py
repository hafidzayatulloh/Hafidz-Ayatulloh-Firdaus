from random import sample

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = sample(items, 4)

print(
    "Tiket apa pun yang cocok dengan empat angka atau huruf ini "
    f"menang hadiah: {winning_ticket}"
)