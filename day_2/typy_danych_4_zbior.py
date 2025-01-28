# zbiór (set) - przechowuje unikalne wartości (brak duplikatów)
# nie zachowuje kolejności przy dodawaniu elementów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # zamiana na zbiór
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# pusty zbior
zb2 = set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(18)
zbior.add(33)
zbior.add(24)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop() - usunięcie pierwszego elementu
print(zbior.pop())
print(zbior)
print(zbior.pop())
# 33
# {66, 777, 11, 44, 18, 22, 24}
# 66
zmienna = zbior.pop()
print("Usunęliśmy element:", zmienna)  # Usunęliśmy element: 777

zbior_copy = zbior.copy()
print(zbior_copy)  # {18, 22, 24, 11, 44}
print(zbior)  # {11, 44, 18, 22, 24}
print(id(zbior))  # 2749828112544
print(id(zbior_copy))  # 2749828108064

# operaacje na zbiorach
zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(type(zbior_2))  # <class 'set'>
print(zbior_2)  # {18, 667, 52, 11, 44, 12.34, 62}

# suma zbiorów - zwraca nowy zbiór
print(zbior | zbior_2)  # {11, 44, 12.34, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {11, 44, 12.34, 18, 52, 22, 24, 667, 62}

# cczęśc wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica
print(zbior - zbior_2)  # {24, 22}
print(zbior.difference(zbior_2))  # {24, 22}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# łaczy zbiory, zmmienia bazowy!!!
zbior.update(zbior_2)
print(zbior)  # {11, 44, 12.34, 18, 52, 22, 24, 667, 62}

krotka = tuple(zbior)
print(krotka)  # (11, 44, 12.34, 18, 52, 22, 24, 667, 62)

lista = list(zbior)
print(lista)  # [11, 44, 12.34, 18, 52, 22, 24, 667, 62]

# sprawdzamy czy dany element istnieje w kolekcji
print(667 in zbior)  # True
print(777 in lista)  # False
print(777 in krotka)  # False
