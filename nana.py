print("Hello World")
print("Hello World")
print("Hello World")
print("AKU VINA")

def vina():
    while True:
        data = input("Siapa nama kamu?")
        if data == "Vina".lower():
            print("Halo Vina")
            continue
        elif data == "Violet".lower():
            print("Halo Violet")
            continue
        elif data == "Suna".lower():
            print("Halo Suna")
            continue
        else:
            print("Maaf, nama kamu tidak dikenal")
            break

vina()