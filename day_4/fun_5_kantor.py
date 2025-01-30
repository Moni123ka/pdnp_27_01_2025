# stworzyc funkcję kantor
# ma mieć dwie wewnętrne funkcje usd, eur
# w zależności od parametru zwracamy funkcje usd lub eur

def kantor(waluta):
    def usd(kwota):
        return 4.1 * kwota

    def eur(kwota):
        return 4.2 * kwota

    if waluta == "usd":
        return usd
    else:
        return eur


kantor_eur = kantor('eur')
print(kantor_eur(10000))  # 42000.0
kantor_usd = kantor('usd')
print(kantor_usd(5000))  # # 20500.0
