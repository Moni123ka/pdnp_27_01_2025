# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku wykona jeden lub drugi blok programu
# warunek musi zwracac typ bool
# Indent Rainbow Plugin

# odp = True
odp = False
if odp:  # debbuger
    # blok programu, który wykonuje się gdy warunek True
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Kolejna część programu")

odp = "Radek"
print(bool(odp))  # True

if odp:
    print("Dane zostały odebrane")
# Dane zostały odebrane

if odp == "Radek":  # == porównanie
    print("Nadal Radek")
    # Nadal Radek

odp = 0  # -> False
if odp:
    print("Działa")
else:  # w przeciwnym przypadku
    print("Zero -> False")
# Zero -> False

a = "Radek"
if len(a) > 3:
    print(f"Długość wynosi {len(a)}, więcej niż 3")
# Długość wynosi 5, więcej niż 3

a = "Radek"
n = len(a)
if n > 3:
    print(f"Długość wynosi {n}, więcej niż 3")
    # Długość wynosi 5, więcej niż 3

# operator morsa :=, walrus operator
if (n := len(a)) > 3:
    print(f"Długość wynosi {n}, więcej niż 3")
# Długość wynosi 5, więcej niż 3


# kolejność warunków ma zanczenie
# pierwszy true kończy sprawdzanie pozostałych
podatek = 0
zarobki = int(input("Podaj zarobki"))
if zarobki < 10_000:
    podatek = 0
elif zarobki < 40_000:
    podatek = 0.2
elif zarobki < 100_000:
    podatek = 0.4
else:
    podatek = 0.9

print(f"Podatek wynosi {podatek * zarobki} pln. wynosi {podatek * 100} %")
# Podatek wynosi 22715.600000000002 pln. wynosi 40.0 %
# podatek 0.2 dla przedziału 10_000 do 39_999
