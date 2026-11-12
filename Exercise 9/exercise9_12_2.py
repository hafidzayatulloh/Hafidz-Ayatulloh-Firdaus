from exercise9_12 import User


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