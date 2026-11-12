class User:
    def __init__(self, first_name, last_name, age, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Kota: {self.city}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali.")


user_1 = User('Budi', 'Santoso', 25, 'Semarang', 'budi@contoh.com')
user_2 = User('Sari', 'Wulandari', 22, 'Surakarta', 'sari@contoh.com')
user_3 = User('Andi', 'Pratama', 30, 'Yogyakarta', 'andi@contoh.com')

for user in (user_1, user_2, user_3):
    user.describe_user()
    user.greet_user()
    print()