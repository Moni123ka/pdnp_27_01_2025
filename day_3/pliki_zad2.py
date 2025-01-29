import chardet

# pythonowy menadżer pakietów pip
# pip install chardet

with open('test.log', "r", encoding="utf-8") as f:
    raw_data = f.read()

print(raw_data)
# Powitanie
# Kolejne
# Jeszcze jedno
# Dopisane
# Dopisane
# Dopiśane

# rb - dane bajtowe, wymagania biblioteki chardet
with open('test.log', "rb") as f:
    raw_data = f.read()

print(raw_data)
# b'Powitanie\r\nKolejne\r\nJeszcze jedno\r\nPowitanie\r\nKolejne\r\nJeszcze jedno\r\nDopisane\r\nDopisane\r\nDopi\xc5\x9bane\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'MacRoman', 'confidence': 0.6642342342342342, 'language': ''}
# Po dodaniu dodatkowych polskich znaków do pliku odczytał kodowanie prawidłowo
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}
encoding = result['encoding']
confidence = result['confidence']

print("Kodowanie:", encoding)  # Kodowanie: utf-8
print("Trafność:", confidence)  # Trafność: 0.938125

print(raw_data.decode(encoding=encoding))
# Powitanie
# Kolejne
# Jeszcze jedno
# Powitanie
# Kolejne
# Jeszcze jedno
# Dopisane
# Dopisane
# Dopiśćąźane
