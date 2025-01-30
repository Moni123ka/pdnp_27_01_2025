# funkcja lambda
# skrócony zapis funkcji
# domyślnie ma return

def odejmij(a, b):
    return a - b


print(odejmij(5, 89))

odejmi2 = lambda a, b: a - b
print(odejmi2(7, 89))

# jak zamienic na lambdę
# def oblicz_vat(kwota, vat=23):
#     return kwota * (100 + vat) / 100

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(1000))  # 1230.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 4, 24, 50, 100, 500]
l = []
for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 6, 8, 48, 100, 200, 1000]

print([i * 2 for i in lista])  # [2, 4, 6, 8, 48, 100, 200, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 6, 8, 48, 100, 200, 1000]

# funkcje wyższego rzędu - przyjmują inną funkcje jako argument
# map() - bierze elementy kolekcji i wykonuje na nich operację zadaną funkcją
print(f"Zastosowanie map(): {list(map(zmien, lista))}")  # Zastosowanie map(): [2, 4, 6, 8, 48, 100, 200, 1000]

# zastosowanie lambdy jako funkcja anonimowa
# użycie w miejscu deklaracji
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 48, 100, 200, 1000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
# Zastosowanie map(): [4, 8, 12, 16, 96, 200, 400, 2000]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)
print(l3)  # [1, 2]

# filter() - zwraca elelemnty spełniające warunek zadany funkcją
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")  # Zastosowanie filter(): [1, 2]
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 50, lista))}")  # Zastosowanie filter(): [1, 2, 3, 4, 24]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 20, lista))}")  # Zastosowanie filter(): [24, 50, 100, 500]
# x > 3 i x < 150
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 150, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 150, lista))}")
# Zastosowanie filter(): [4, 24, 50, 100]
# Zastosowanie filter(): [4, 24, 50, 100]
