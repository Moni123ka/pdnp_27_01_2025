# funkcje zwracające wynik
# kończy się słówkiem return
# gdy napotka na return kończy działanie funkcji


def dodaj(a, b):
    return a + b


def odejmij(a, b=0, c=0):
    return a - b - c


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(dodaj(5, 9))  # 14
wynik = dodaj(89, 56)
print("Wynik", wynik)

# na kilka sposobów uzyc funkcji odejmij
print(odejmij(1))
print(odejmij(1, 2))
print(odejmij(1, 2, 3))
print(odejmij(b=9, a=10))
print(odejmij(b=9, a=10, c=567))
print(odejmij(1, 2, c=90))

print(oblicz_vat(1000))  # 1230.0
print(oblicz_vat(vat=9, kwota=4500))  # 4905.0
print(oblicz_vat(1000, 15))

zm = oblicz_vat(1000)
print(type(zm))  # <class 'float'>

if zm == 1230:
    print("Ok")  # Ok

print(dodaj(56, 78) + dodaj(45, 67))  # 246
