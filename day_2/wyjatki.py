# wyjątek - błedy podczas wykonania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\Administrator\PycharmProjects\pdnp_27_01_2025\day_2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
lista = []
try:
    # print(5 / 0)
    # print("A" * "23")
    # print(lista[10])
    # raise KeyError("Brak klucza")  # rzucić bład (wyjątek)
    wynik = 90 / 33
except ZeroDivisionError:
    print("Nie dziel przez zero!!!")
except TypeError:
    print("Błąd typu")
except IndexError:
    print("Nie ma elementu w liście")
except Exception as e:
    print("Bład", e)
else:  # gdy nie ma błedu
    print("Wynik", wynik)
finally:
    print("Działa zawsze")

print("Program nadal działa")
# Nie dziel przez zero!!!
# Program nadal działa
# Bład 'Brak klucza'
# Program nadal działa
# Wynik 2.727272727272727
# Program nadal działa
# Wynik 2.727272727272727
# Działa zawsze
# Program nadal
# Nie ma elementu w liście
# Działa zawsze
# Program nadal działa

# try - except [else - finally]
