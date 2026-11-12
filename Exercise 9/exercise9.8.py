class User:
    def __init__(self, first_name, last_name, age, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Kota: {self.city}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
                'dapat menambah postingan',
                'dapat menghapus postingan',
                'dapat memblokir pengguna',
            ]
        self.privileges = privileges

    def show_privileges(self):
        print("Hak akses admin:")
        for privilege in self.privileges:
            print(f"    - {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, city, email):
        super().__init__(first_name, last_name, age, city, email)
        self.privileges = Privileges()


admin = Admin('Andi', 'Pratama', 30, 'Yogyakarta', 'andi@contoh.com')

admin.privileges.show_privileges()