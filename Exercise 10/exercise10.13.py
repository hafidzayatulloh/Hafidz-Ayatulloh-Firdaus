from pathlib import Path
import json


def get_stored_user(path):
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        return json.loads(contents)
    return None


def get_new_user(path):
    user = {
        'name': input("Siapa namamu? "),
        'city': input("Kamu tinggal di kota mana? "),
        'hobby': input("Apa hobimu? "),
    }
    contents = json.dumps(user)
    path.write_text(contents, encoding='utf-8')
    return user


def remember_user():
    path = Path(__file__).parent / 'user_info.json'
    user = get_stored_user(path)

    if user:
        print("Selamat datang kembali!")
    else:
        user = get_new_user(path)
        print("Aku akan mengingatmu.")

    print("\nYang aku ingat tentangmu:")
    print(f"    Nama: {user['name']}")
    print(f"    Kota: {user['city']}")
    print(f"    Hobi: {user['hobby']}")


remember_user()