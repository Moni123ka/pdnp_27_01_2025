# działania z plikami
# filehandler - rura do pliku
# context manager - pomaga w pracy z szasobanmi np.: plikami
# with - context manager


# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open("test.log", "w", encoding="utf-8") as fh:  # fh - filehandler
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")

# "x" rzuca bład gdy plik istnieje
# with open('test.log', "x", encoding="utf-8") as f:
#     f.write("Powitanie\n")
# Traceback (most recent call last):
#   File "C:\Users\Administrator\PycharmProjects\pdnp_27_01_2025\day_3\pliki_zad1.py", line 23, in <module>
#     with open('test.log', "x") as f:
#          ^^^^^^^^^^^^^^^^^^^^^
# FileExistsError: [Errno 17] File exists: 'test.log'

# "W" jeśli plik istnieje zostanie usunięty
with open("test.log", "w", encoding="utf-8") as fh:  # fh - filehandler
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")

# "a" dopisanie na końcu pliku
with open("test.log", "a", encoding="utf-8") as fh:  # fh - filehandler
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")
    fh.write("Dopisane\n")
    fh.write("Dopisane\n")
    fh.write("Dopiśane\n")

# "r" odczyt pliku
with open("test.log", "r", encoding="utf-8") as file:
    lines = file.read()

print(lines)
# Jeszcze jedno
# Powitanie
# Kolejne
# Jeszcze jedno
# Dopisane
# Dopisane
