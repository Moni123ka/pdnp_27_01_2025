tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))  # <class 'str'>

# teksty są niemutowalne
tekst.upper()
print(tekst)  # Witaj Świecie
""" Return a copy of the string converted to uppercase. """
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)
print(tekst_upper)
print(tekst_upper)

# małe litery, capitalize
print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie
print(tekst.swapcase())  # wITAJ śWIECIE

print(tekst)  # Witaj Świecie
# Witaj Świecie
# 01234567890... - indeksy numerowane od 0

print(tekst[6])  # "Ś"

print(tekst.index("Ś"))  # 6
print(tekst.index("i"))  # indeks numer 1
print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("j", 0, 4))  # wystepuje 0 razy, bo z prawej strony zbiór otwarty, 0123
print(tekst[4])  # j

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# usunięcie biłaych znaków, spacji.. -> strip()
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

tekst_zamiana = "Witaj Dobry Świecie"
print(tekst_zamiana.replace("Dobry", ""))  # "Witaj  Świecie"
