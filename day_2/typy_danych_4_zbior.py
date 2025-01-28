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
