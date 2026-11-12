from pathlib import Path

filenames = ['Mothers_still.txt', 'roman.txt', 'Blue_law.txt']

for filename in filenames:
    path = Path(__file__).parent / filename

    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"\nMaaf, file {filename} tidak ditemukan.")
    else:
        lowered = contents.lower()
        count_the = lowered.count('the')
        count_the_space = lowered.count('the ')

        print(f"\n{filename}")
        print(f"    'the'  : {count_the} kali")
        print(f"    'the ' : {count_the_space} kali")