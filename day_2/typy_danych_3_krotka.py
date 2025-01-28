# krotka - tuple - kolekcja niemutowalna, tylko do odczytu
# pozwala efektywniej zarządzać pamięcią
# krotka jednoelementowa  - zastępstwo stałych, zmienna niezmienna

tupla_imiona = "Radek", "Tomek", "Zenek", "Mateusz", 'Ania', "Marek"
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Mateusz', 'Ania', 'Marek')
print(type(tupla_imiona))  # <class 'tuple'>

tupla_liczby = 43, 55, 22.34, 11, 200
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>

tupla_liczby = (43, 55, 22.34, 11, 200)
print(tupla_liczby)
print(type(tupla_liczby))
# (43, 55, 22.34, 11, 200)
# <class 'tuple'>

# tupla jednoelementowa
tupla = 43,
print(tupla)
print(type(tupla))
# (43,)
# <class 'tuple'>

# PEP8 zaleca tworzenie tupli jednoelementowej z nawiasami ()
tupla = (43,)
print(tupla)
print(type(tupla))
# (43,)
# <class 'tuple'>

# tupla jest niemutowalna
# tupla_liczby[3] = 123 # TypeError: 'tuple' object does not support item assignment

del tupla_liczby
# print(tupla_liczby) # NameError: name 'tupla_liczby' is not defined

print(tupla_imiona.index("Radek"))  # index 0
print(tupla_imiona.count("Radek"))  # występuje jeden raz

# rozpakowanie tupli
tup = 1, 2
print(type(tup))  # <class 'tuple'>

a, b = 1, 2
print(a, b)  # 1 2

a, b = tup  # 1, 2
print(a, b)  # 1 2

tup_2 = 1, 2, 3
# a, b = tup_2  # ValueError: too many values to unpack (expected 2)
a, *b = tup_2
print(a, b)  # 1 [2, 3] * worek na pozostałe dane, lista

print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Mateusz', 'Ania', 'Marek')
print(len(tupla_imiona))  # 6
*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Radek', 'Tomek', 'Zenek', 'Mateusz'] Ania Marek

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Radek ['Tomek', 'Zenek', 'Mateusz', 'Ania'] Marek

name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Radek Tomek ['Zenek', 'Mateusz', 'Ania', 'Marek']

# sortowanie krotki zwraca posortowaną listę
# nie zmienia krotki
print(sorted(tupla_imiona))  # ['Ania', 'Marek', 'Mateusz', 'Radek', 'Tomek', 'Zenek']
print(tupla_imiona)
