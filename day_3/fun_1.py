# funkcja - wykonuje fragment kodu w dowolnym momencie
# funkcja musi być najpierw zadeklarowana
# w miejscu deklaracji funkcja nie wykonuje się!!!
# żeby uruchomić funkcję należy ją wywołać

# Funkcje niezwracające wyniku
# argumenty globalne
a = 8
b = 6


# PEP8 zaleca by definicję funkcji od ciła programu dzieliły dwie puste linie
# deklaracja funkcji
def dodaj():  # funkcja bez argumentów
    print(a + b)  # wypisz wynik dodawania


def dodaj2(a, b):  # argumenty a i b obowiązkowe do przekazania
    # argumenty lokalne o nazwie a i b
    print(a + b)


# symulujemy możliwośc uzycia funkcji z różną liczbą argumentów
def odejmij(a, b, c=0):  # c - argument o wartości domyślnej
    print(a - b - c)


# użycie funkcji (uruchomienie)
# nazwa funkcji i nawiasy ()
dodaj()  # 14
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

# przekazywanie argumentów pozycyjne (po pozycji)
dodaj2(67, 89)  # 156
odejmij(12, 2)  # 10, c=0
odejmij(12, 2, 7)  # 3, c=7

# argumenty po nazwie
odejmij(c=9, b=8, a=10)  # -7
dodaj2(b=9, a=3)  # 12

# argumenty mieszane
odejmij(1, 2, c=9)  # -10
# argumenty pozycyjne muszą być przed nazwanymi!!!
# odejmij(a=6, 3, 4) # SyntaxError: positional argument follows keyword argument

print(dodaj())
# 14
# None

# print(dodaj() + dodaj())
# None + None # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
