my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("Makanan favorit saya adalah:")
for food in my_foods:
    print(food)

print("\nMakanan favorit teman saya adalah:")
for food in friend_foods:
    print(food)