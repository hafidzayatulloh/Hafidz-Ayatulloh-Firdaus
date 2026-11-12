class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"{self.restaurant_name} menyajikan "
            f"masakan {self.cuisine_type}."
        )

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print(f"Rasa es krim yang tersedia di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"    - {flavor}")


stand = IceCreamStand(
    'Es Krim Segar', 'es krim', ['vanila', 'cokelat', 'stroberi']
)

stand.describe_restaurant()
stand.show_flavors()