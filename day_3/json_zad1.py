# {"name":"John", "age":30, "car":null}
# dane typu klucz wartość
# uzywany jest do komunikacji w internecie
# odpowiednikiem jsona w pythonie jest słownik

import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
# {"name": "Radek", "age": 40, "czy_pali": null}

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)

# upiększenie, beautify
with open('nasze_dane_b.json', "w") as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# posortowane klucze
with open('nasze_dane_sort.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# # {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open("nasze_dane.json", "r") as fh:
    data = json.load(fh)

print(data)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(data))  # <class 'dict'>

print(data['name'])  # Radek

# zamiana słownika na json (str)
json_text = json.dumps(data)
print(json_text)  # {"name": "Radek", "age": 40, "czy_pali": null}
print(type(json_text))  # <class 'str'>

dict_json = json.loads(json_text)
print(dict_json)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(dict_json))  # <class 'dict'>

# wypisac klucze ze słownika dict_json
for k in dict_json:
    print("Klucz:", k)
# Klucz: name
# Klucz: age
# Klucz: czy_pali
