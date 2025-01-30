a = 10  # globalne
b = 10


def dodaj():
    a = 7  # lokalne zmienne
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # uzyje globalnych


def dodaj3():
    global a
    a = 9  # nadpisze globalne a, zmieni wartośc a globalnego
    b = 89
    print(a + b)


print(f"WArtość a z góry {a=} (globalna)")  # WArtość a z góry a=10 (globalna)
dodaj()  # 15
print(f"WArtość a z góry {a=} (globalna)")  # WArtość a z góry a=10 (globalna)
dodaj2()  # 20 działanie na globalnych zmiennych
print(f"WArtość a z góry {a=} (globalna)")  # WArtość a z góry a=10 (globalna)
dodaj3()  # 98, zmieniło wartość a globalnego
print(f"WArtość a z góry {a=} (globalna)")  # WArtość a z góry a=9 (globalna)
dodaj2()  # 19
print(f"WArtość a z góry {a=} (globalna)")  # WArtość a z góry a=9 (globalna)
