from abc import ABC, abstractmethod


# klasa abstrakcyjna
class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # oznaczenie, ze metoda abstrakcyjna
    def wydaj_glos(self):
        pass


class Kura(Ptak):
    """
    Tu kura
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # obowiązkowo musimu wywołac konstruktor z kalsy wyzszej (super())

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_glos(self):
        print("Ko ko ko ko ko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


# klasa Orzel
# kir kier kir
class Orzel(Ptak):
    """
    Klasa Ptak
    """

    def wydaj_glos(self):
        print("Kir kier kir")

    def polowanie(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie.")


class Sowa(Ptak):
    """
    Klasa Sowa
    """


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_glos'
# or1 = Ptak("Orzel", 45)
# or1.latam()  # Tu Orzel Lecę z szybkością 45
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam.
kur2.wydaj_glos()  # Ko ko ko ko ko

or2 = Orzel("Orzel Bielik", 50)
or2.latam()
or2.wydaj_glos()
# Tu Orzel Bielik Lecę z szybkością 50
# Kir kier kir
kur2.dziobanie()
or2.polowanie()
# Tu Kura domowa Idę sobie podziobać
# Tu Orzel Bielik Rozpoczynam polowanie.

# polimorfizm - wspolne metody dla obiektów róznych klas
# wynikaj z dziedziczenia i wymuszenia poprzez metode abstrakcyjną
lista = [kur2, or2]  # obiekty róznych klas
for i in lista:
    i.latam()
# Tu Kura domowa Ja nie latam.
# Tu Orzel Bielik Lecę z szybkością 50

# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_glos'
# sowa = Sowa("Sowa", 15)
