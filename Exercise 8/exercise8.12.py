def make_sandwich(*items):
    print("\nMembuat sandwich dengan isian:")
    for item in items:
        print(f"    - {item}")


make_sandwich('tuna', 'keju')
make_sandwich('ayam', 'selada', 'tomat', 'mayones')
make_sandwich('telur')