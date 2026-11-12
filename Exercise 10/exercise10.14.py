from pathlib import Path
import json


def get_stored_username(path):
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        return json.loads(contents)
    return None


def get_new_username(path):
    username = input("Siapa namamu? ")
    contents = json.dumps(username)
    path.write_text(contents, encoding='utf-8')
    return username


def greet_user():
    path = Path(__file__).parent / 'username.json'
    username = get_stored_username(path)

    if username:
        correct = input(f"Apakah kamu {username}? (y/n) ")
        if correct == 'y':
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username(path)
            print(f"Kami akan mengingatmu saat kamu kembali, {username}!")
    else:
        username = get_new_username(path)
        print(f"Kami akan mengingatmu saat kamu kembali, {username}!")


greet_user()