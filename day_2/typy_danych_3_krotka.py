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
