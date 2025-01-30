class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca - konstruktor
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

        # self - obiekt, który wywołuje metode np.: cz1

    def powitanie(self):
        print(f'Nazywam się {self.imie}')
        # print(f'Nazywam się {cz1.imie}')

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat/a.")

    # wypisz_wzrost()
    def wypisz_wzrost(self):
        print(f"Mój wzrost wynosi {self.wzrost} cm.")

    def ruszaj(self):

        if self.plec == "k":
            print("Ruszyałam w drogę")
        else:
            print("Ruszyłem w drogę")


# cz1 = Human() # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Radek", 67, 190, "m")
cz1.powitanie()
cz1.wypisz_wiek()
# Nazywam się Radek
# Mam 67 lat/a.
cz1.wypisz_wzrost()  # Mój wzrost wynosi 190 cm.
cz1.ruszaj()  # Ruszyłem w drogę

cz2 = Human("Anna", 45, 178)
cz2.powitanie()
cz2.ruszaj()
# Nazywam się Anna
# Ruszyałam w drogę
