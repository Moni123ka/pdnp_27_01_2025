# słownik - para klucz wartość
# {"user": "Radek", 'wiek': 76}
# klucze nie mogą się powtarzać
# odpowiednik json

# pusty słownik
dictionary = dict()
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = {}
print(type(dictionary_1))  # <class 'dict'>
print(dictionary_1)  # {}

# dodanie elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 48
print(dictionary)  # {'imie': 'Radek', 'wiek': 48}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 48])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 48)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 48}

# wypisanie wartości dla klucza
print(dictionary['imie'])  # Tomek

# print(dictionary["Imie"])  # KeyError: 'Imie'
print(dictionary.get("Imie"))  # None, nie ma klucza
print(dictionary.get("Imie", "default"))  # default, nie ma klucza

dictionary.update({'data': '12-12-2025'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 48, 'data': '12-12-2025'}

dict_small = {'x': 2}
print(dict_small)  # {'x': 2}
dict_small.update([('y', 3), ("z", 5)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 5}

