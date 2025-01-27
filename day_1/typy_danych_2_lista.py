# kolekcje

# lista - przechowuje dowolną ilość danych, różnego typu na raz
# zachowuje kolejnosć przy dodawaniu danych

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodawanie elemntów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Bogdan")
lista.append("Anna")
lista.append("Maciek")
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Bogdan', 'Anna', 'Maciek']
# ['Radek', 'Tomek', 'Zenek', 'Bogdan', 'Anna', 'Maciek']
#    0         1        2        3         4       5
#    -6        -5      -4       -3         -2      -1
print(len(lista))  # 6
print(lista[0])  # Radek
print(lista[2])  # Zenek
print(lista[4])  # Anna

# print(lista[10]) # IndexError: list index out of range

print(lista[5])  # Maciek
print(lista[len(lista) - 1])  # Maciek
print(lista[-1])  # Maciek, ostatni element z listy
print(lista[-3])  # Bogdan

# wyświetlanie fragmentu listy (slicowanie)
print(lista[0:3])  # ['Radek', 'Tomek', 'Zenek'], indeksy 012
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek'], indeksy 012
print(lista[2:])  # [['Zenek', 'Bogdan', 'Anna', 'Maciek'] 2345
print(lista[2:5])  # ['Zenek', 'Bogdan', 'Anna'] 234

print(lista[2:16])  # ['Zenek', 'Bogdan', 'Anna', 'Maciek']
print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Bogdan', 'Anna', 'Maciek']
print(lista[2:2])  # []
print(lista[2:3])  # ['Zenek']
print(lista[10:27])  # []

# ['Radek', 'Tomek', 'Zenek', 'Bogdan', 'Anna', 'Maciek']
#    0         1        2        3         4       5
#    -6        -5      -4       -3         -2      -1

print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # [0:4] # ['Radek', 'Tomek', 'Zenek', 'Bogdan']

lista_15 = list(range(15))  # 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[0:15:2])  # [start:stop:krok] [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(0, 15, 2)))  # (start, stop, krok) [0, 2, 4, 6, 8, 10, 12, 14]
print(lista[::2])  # ['Radek', 'Zenek', 'Anna'], co drugi element

print(lista[::-1])  # krok w tył, wypisana odwrócona lista
# ['Maciek', 'Anna', 'Bogdan', 'Zenek', 'Tomek', 'Radek']
