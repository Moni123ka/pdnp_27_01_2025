# klasa - element programowania obiektowego
# klasa - szablon, opis, przepis wg którego będą budowane obiekty
# cechy - pola (zmienne)
# metody - funkcje możkliwe do wykonaniana obiektach
# obiekt - instancja klasy
# klasa musi byc zadaklarowana przed użyciem
# tworzenie obietku uruchamia metote __init__ w klasie
# paradygmaty -> hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PascalCase -> PEP8
class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    # self - obiekt, który wywołuje metode np.: cz1
    def powitanie(self):
        print(f'Nazywam się {self.imie}')
        # print(f'Nazywam się {cz1.imie}')

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat/a.")


print(Human.__doc__)  # Klasa Human opisująca człowieka w Pythonie
help(Human)
# #
#     Klasa Human opisująca człowieka w Pythonie
#
# Help on class Human in module __main__:
#
# class Human(builtins.object)
#  |  Klasa Human opisująca człowieka w Pythonie
#  |
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables
#  |
#  |  __weakref__
#  |      list of weak references to the object
print(print.__doc__)
#   sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.

# pydoc -b uruchomienie serwera z dokumentacją
# cd day_4 przejscie do katalogu day_4
# pydoc -w kl1 generowanie pliku html z dokumentacją

# tworzenie obiektu klasy Human
cz1 = Human()
print(cz1)  # <__main__.Human object at 0x00000252F841CCE0>
cz1.imie = "Robert"
cz1.wiek = 37
cz1.plec = "m"

print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Robert
# 37
# m
cz1.powitanie()  # Nazywam się Robert
cz1.wypisz_wiek()  # Mam 37 lat.

cz2 = Human()
print(cz2)  # <__main__.Human object at 0x00000252F841CCE0>
cz2.imie = "Anna"
cz2.wiek = 30

print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Anna
# 30
# k
cz2.powitanie()
cz2.wypisz_wiek()
# Nazywam się Anna
# Mam 30 lat.
