import sys # import pakietu sys - zadania systemowe

print()  # wypisz/wydrukuj
# ctrl alt l - formatowanie kodu
# Process finished with exit code 0 - program zakończył działanie bez błędu

# ctrl d - powielanie linii
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek

print('Nazywam się Radek')  # Nazywam się Radek
# print('Nazywam się Radek")
#   File "C:\Users\Administrator\PycharmProjects\pdnp_27_01_2025\day_1\pierwszy.py", line 15
#     print('Nazywam się Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 15)
#
# Process finished with exit code 1 - zakończone z błędem
# interpretowany, wykonuje się od góry do dołu
# bład zatrzymuje działanie programu

print("Nazywam się 'Radek'")  # Nazywam się 'Radek'

# type() - sprawdzenie typu danych
print(type("Radek")) # <class 'str'>, string, dane typu tekstowego

print("39" + "39") # 3939, konkatenacja, łączenie tekstów

print(39 + 39) # 78 operacja na liczbach
print(type(39)) # <class 'int'>, liczba całkowita, integer
print(sys.int_info) # zakres liczb int
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

# operacja niedozwolona
# nie zamienia typów na inne w trakcie wykonywania operacji
# silne typowanie
# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str

# musimy jawnie wskazac odpowiednie typy
print(int("39")) # rzutowanie, zamian na liczbę int
print(int("39") + 39) # 78
# print(int("A")) # ValueError: invalid literal for int() with base 10: 'A'

print("39" + str(39)) # 3939, str() rzutowanie, zamiana na str

print(5 * "4") # 44444
print("168" * 50)
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168
print(168 * 50)  # 8400
print(int(168) * int(50)) # 8400

