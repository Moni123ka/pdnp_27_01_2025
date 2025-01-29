import random

# operacje na liczbach losowych

print(random.randint(1, 100))  # int 69, od 1 do 100
print(random.randrange(1, 100))  # int 58, od 1 do 99
print(random.randrange(5))  # od 0 do 4
print(random.random())  # 0.9231289538656651 float od 0 do 0.999999
print(random.random() * 7)  # 6.994572940948036 float od 0 do 6.999999

lista = [67, 45, 32, 68, 69, 90, 42]
print(random.choice(lista))  # wylosuje element z listy: 67

lista_kule = list(range(1, 50))
# print(lista_kule)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)  # 27

print(random.choices(lista_kule, k=6))  # [8, 31, 31, 45, 43, 20] z powtórzeniami
print(random.sample(lista_kule, k=6))  # [26, 43, 9, 1, 12, 27] # bez powtórzeń
print(random.sample(lista_kule, 6))  # [34, 20, 19, 12, 35, 2]
# ctrl / - komentarze
