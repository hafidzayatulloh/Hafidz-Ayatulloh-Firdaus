class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Mobil ini punya baterai {self.battery_size}-kWh.")

    def get_range(self):
        if self.battery_size == 40:
            distance = 150
        elif self.battery_size == 65:
            distance = 225

        print(f"Mobil ini bisa menempuh sekitar {distance} mil.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()