dictionary = {"imie": "Radek", 'nazwisko': "Kowalski"}
print(type(dictionary))

#  wyświetli klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wyswietla waartości
for i in dictionary.values():
    print(i)
# Radek
# Kowalski

# wyświetli pary
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)
    print(k, v)
# imie => Radek
# nazwisko => Kowalski
# imie => Radek
# imie Radek
# nazwisko => Kowalski
# nazwisko Kowalski
# sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski
for k, v in dictionary.items():
    print(k, v, sep="=>", end="<=>")
# imie=>Radek<=>nazwisko=>Kowalski<=>
print("Radek")  # imie=>Radek<=>nazwisko=>Kowalski<=>Radek to ustawi end="\n"
print("Tomek")
# imie=>Radek<=>nazwisko=>Kowalski<=>Radek
# Tomek

pol_ang = {"kot": 'cat', 'pies': "dog", 'dach': "roof"}
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)  # {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}

print({value: key for key, value in pol_ang.items()})
# {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}

# test Tabnine
print({value: key for key, value in pol_ang.items()})
print({value: key for key, value in pol_ang.items()})
print()  # {'cat': 'kot', 'dog': 'pies',   '           '}
# zrób pętlę po słowniku
for k, v in pol_ang.items():
    print(f"{k}: {v}")
    print(f"{v}: {k}")
# zrób pętle i wypisz wszystkie pary opisując eleemnty
for k, v in pol_ang.items():
    print(f"{k}: {v} => {ang_pol[v]}")
# kot: cat => kot
# pies: dog => pies
# dach: roof => dach
# coopilot
