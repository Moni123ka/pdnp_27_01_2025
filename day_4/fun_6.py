# stworzyc funkcję obliczającą średnią

def liczby(*cyfry):  # dowolna ilosć argumentów pozycyjnych
    print(cyfry)
    count = len(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
    except Exception as e:
        print("Bład:", e)
    else:
        print(f"Średnia wynosi {avg}")
    finally:
        print("Obliczenia zakończone")


liczby()  # ()
liczby(1, 2, 3, 4, 5, 6)  # (1, 2, 3, 4, 5, 6)
# ()
# Bład: division by zero
# Obliczenia zakończone
# (1, 2, 3, 4, 5, 6)
# Średnia wynosi 3.5
# Obliczenia zakończone
