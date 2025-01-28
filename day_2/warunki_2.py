# python 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.strip().casefold():
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("Znam Jave")
    case _:  # wartość domyślna, odpowiednik else
        print("Nie znam takiego języka")

print(lista)
# Podaj znany Ci język programowaniaexcel
# Nie znam takiego języka
# []
