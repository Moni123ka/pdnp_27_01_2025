class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizująca
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        # pole jest prywatne, brak dostępu poza klasą
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h.")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __zmien_bieg(self):
        print("Zmiana biegu")


car = Car("Opel", 2025)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# dal pola prywatnego nie ma dostępu do pola z obiektu
# print(car.__predkosc)  # 50
car.licznik()  # Prędkość wynosi 50 km/h.
car.__predkosc = 0  # pole publiczne o tej samej nazwie ale inne
car.licznik()  # Prędkość wynosi 50 km/h.
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()  # Prędkość wynosi 0 km/h.
print(car.__predkosc)  # 0 publiczne
# Prędkość wynosi 50 km/h.
# Prędkość wynosi 50 km/h.
# Zmiana biegu -> metoda prywatna __zmien_bieg()
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkość wynosi 0 km/h.
# 0
