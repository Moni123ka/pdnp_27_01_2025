# pętle - możliwośc wykonanina kodu wielokrotnie
# for - pętla iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(20):  # niema zmienna
    print("Test podłoga")
    # print(_)  # 19

for i in range(5):
    print(i * 2)
    print(i + 2)

# przerobic lotto na pętlę
lista_kule = list(range(1, 50))  # lista zawierająca nasze "kule"
# print(lista_kule)
lista_wyn = []  # lista wyników
for _ in range(6):  # 012345 wykona 6 razy
    wyn = random.choice(lista_kule)  # losuje liczbę z listy(element listy)
    lista_kule.remove(wyn)  # usunie kule z listy, żeby nie było powtórzeń
    # print(wyn)  # 27
    lista_wyn.append(wyn)  # dodaje kule do listy z wynikami losowania

print("Wynik losowania:", lista_wyn)  # Wynik losowania: [48, 35, 9, 15, 31, 16]

for i in range(10):
    if i % 2 == 0:
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

lista3 = []
for j in range(10):
    if j % 2 == 0:
        lista3.append(j)
print(lista3)  # [0, 2, 4, 6, 8]

# list comprehension
lista3 = [j for j in range(10) if j % 2 == 0]

# [0, 2, 4, 6, 8]
for c in lista3:  # pobieraj z listy az do ostatniego elementu
    if c > 4:
        print("Większe od 4")
    else:
        print('Mniejsze, równe 4')
# Mniejsze, równe 4
# Mniejsze, równe 4
# Mniejsze, równe 4
# Większe od 4
# Większe od 4

for i in range(0, 10, 2):  # (start, stop, krok) krok 2, co drugi element
    print(i)

for i in range(-10, 0):  # bez 0
    print(i)

for i in range(10, 0, -2):  # od 10 do 1 bez zera co drugi, w dół
    print(i)
# 10
# 8
# 6
# 4
# 2
# # [0, 2, 4, 6, 8]
for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
        print(c)  # tylko gdy warunek spełniony
    print("Przy każdym przejściu pętli")
# Przy każdym przejściu pętli
# 3
# Przy każdym przejściu pętli
# Przy każdym przejściu pętli
# Przy każdym przejściu pętli
# Przy każdym przejściu pętli
print("Po wykonaniu pętli:", c)  # Po wykonaniu pętli: 8

imiona = ["Radek", "Tomek", "Zenek", "Ania"]
print(imiona)  # ['Radek', 'Tomek', 'Zenek', 'Ania']
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# 0 Radek
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i in range(len(imiona)):  # range(4) -> 0123
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enamurete() - numeruje kolekcje i zwraca element i numer
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')

for i, p in enumerate(imiona):
    print(i, p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i, p in enumerate(imiona, start=1):
    print(i, p)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

imiona = ["Radek", "Tomek", "Zenek", "Ania", "Ewa"]
wiek = [44, 55, 32, 27]
# Radek 44
# for p in imiona:
#     print(p, wiek[imiona.index(p)])
# Radek 44
# Tomek 55
# Zenek 32
# Ania 27
# gdy listy mają różną długość dostaniemy błąd: IndexError: list index out of range

# zip() - łaczy kolekcje
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Ania', 27)
for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 44
# Tomek 55
# Zenek 32
# Ania 27

# 0 Radek 44
for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 55))
# (2, ('Zenek', 32))
# (3, ('Ania', 27))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(a, c, d)  # 0 Radek 44
(a, (c, d)) = (0, ('Radek', 44))
print(a, c, d)  # 0 Radek 44
# i, (o, w) = (0, ('Radek', 44)) -> 0 Radek 44
for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 44
# 1 Tomek 55
# 2 Zenek 32
# 3 Ania 27
