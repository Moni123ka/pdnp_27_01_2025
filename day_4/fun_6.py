# stworzyc funkcję obliczającą średnią

def liczby(name=None, *cyfry):  # dowolna ilosć argumentów pozycyjnych
    print(cyfry)
    count = len(cyfry)
    suma = 0
    suma_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = suma_p / count
    except Exception as e:
        print("Bład:", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi {avg}")
        print(f"Średnia dla ucznia {name} wynosi {avg_p}")
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
# ("Radek", 1,2,3,4,5,6) -> name, *cyfry
liczby("Radek", 1, 2, 3, 4, 5, 6)
# (1, 2, 3, 4, 5, 6)
# Średnia dla ucznia Radek wynosi 3.5
# Obliczenia zakończone
# ()
# Bład: division by zero
# Obliczenia zakończone
# (2, 3, 4, 5, 6)
# Średnia dla ucznia 1 wynosi 4.0
# Średnia dla ucznia 1 wynosi 4.0
# Obliczenia zakończone
# (1, 2, 3, 4, 5, 6)
# Średnia dla ucznia Radek wynosi 3.5
# Średnia dla ucznia Radek wynosi 3.5
# Obliczenia zakończone
