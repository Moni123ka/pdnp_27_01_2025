user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # <class 'float'> - liczby zmiennoprzecinkowe
print(type(wersja))  # <class 'float'>
liczba = 456789123098  # int

print("Witaj %s, masz teraz %d lat." % (user, wiek))  # Witaj Tomek, masz teraz 39 lat.
# sprawdza typy
# print("Witaj %d, masz teraz %s lat." % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %f: formatowanie liczb zmiennoprzecinkowych
# %d: formatowanie liczb całkowitych
# %s - łańcuch znaków (string)
# pod klucz "user" wstawiamy wartosć ze zmiennej user
print("Witaj %(user)s, jesteś %(user)s" % {"user": user})
# Witaj Tomek, jesteś Tomek
print("Witaj %(user)a, jesteś %(user)a" % {"user": user})
# Witaj 'Tomek', jesteś 'Tomek'

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.

print("Używamy wersji pythona %i" % 3)  # Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3)  # Używamy wersji pythona 3.000000
print("Używamy wersji pythona %f" % 3.9)  # Używamy wersji pythona 3.900000
print("Używamy wersji pythona %.2f" % 3.9)  # Używamy wersji pythona 3.90
print("Używamy wersji pythona %.1f" % 3.9)  # Używamy wersji pythona 3.9
print("Używamy wersji pythona %.0f" % 3.9)  # Używamy wersji pythona 4 zaokrągla do wyświetlenia
print("Używamy wersji pythona %.f" % 3.9)  # Używamy wersji pythona 4 zaokrągla do wyświetlenia
x = 3.8796
print(x)  # 3.8796
print("%.2f" % x)  # 3.88
print(x)  # 3.8796

y = round(x)
print(y)  # 4

z = round(x, 2)
print(z)  # 3.88

print(f"Używamy wersji pythona {wersja}")  # Używamy wersji pythona 3.900001
print(f"Używamy wersji pythona {wersja:.2f}")  # Używamy wersji pythona 3.90
print(f"Używamy wersji pythona {wersja:.1f}")  # Używamy wersji pythona 3.9
print(f"Używamy wersji pythona {wersja:.0f}")  # Używamy wersji pythona 4

print(f"{user:<10}")  # "Tomek     "
print(f"{user:>20}")  # "               Tomek"
print(f"{user:^20}")  # "       Tomek        "

print(liczba)  # 456789123098
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 456,789,123,098
print(f"Nasza duża liczba {liczba:_}")  # Nasza duża liczba 456_789_123_098
print(f"Nasza duża liczba {liczba:_}".replace("_", "."))  # Nasza duża liczba 456.789.123.098
print(f"Nasza duża liczba {liczba:_}".replace("_", " "))  # Nasza duża liczba 456 789 123 098

# liczba = 15000000000000
liczba = 15_000_000_000_000
print(liczba)  # 15000000000000
print(type(liczba))  # <class 'int'>
