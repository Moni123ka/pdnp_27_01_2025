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
# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki} pln. wynosi {podatek * 100} %")
# # Podatek wynosi 22715.600000000002 pln. wynosi 40.0 %
# # podatek 0.2 dla przedziału 10_000 do 39_999

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

rabat = 25 if suma_zam > 100 else 0  # operator warunkowy
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

# zasymulejemy system zbierania logów
# zmienna będzie zawierać informację jaki system przysłął log
# email, console, inny (else)
# gdy log z systemu "console" wyświetlimy napis "Stało się coś strasznego"
# email -> "System email"
# jesli system email to do listy błędów wpisać opis błedu (error -> Krytyczny)
# error -> error, medium, inny

# alert_system = input("System: ").strip().casefold()
# lista_b = []  # pusta lista błędów
#
# if alert_system == "console":
#     print("Stało się coś strasznego")
# elif alert_system == "email":
#     print("System email")
#     error = input("Podaj typ błędu").strip().casefold()  # error, medium, inny
#     if error == "error":
#         lista_b.append('Krytyczny')
#     elif error == "medium":
#         lista_b.append("Ostrzeżenie")
#     else:
#         print("nie znam")
#     print(lista_b)
# else:
#     print("inny")
# System: email
# System email
# Podaj typ błęduerror
# ['Krytyczny']

# napisać program test z...
# zadać pytanie -> input()
# pobrać odpowiedź
# sprawdzić czy odpowiedź jest właściwa i wypisać wynik -> if...
punkty = 0
odp = input("Podaj rok Chrztu Polski")  # str
if odp.strip().casefold() == "966":
    punkty += 1  # punkty = punkty + 1
    print("Dobrze", "zdobyłes pkt: ", punkty)
else:
    print("Idź się pouczyć")

odp = input("Gdzie się odbył?")
if odp.strip().casefold() == "Gniezno".strip().casefold():
    punkty += 1  # punkty = punkty + 1
    print("Dobrze", "zdobyłes pkt: ", punkty)
else:
    print("Tragedia")
print("Razem punktów: ", punkty)
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
