# csv - dane odzielone znakiem podziału
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

import csv

# csv bibliotek do plików csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', '3', '0']
dict = dict(zip(fields, row))
print(dict)
# {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0'}

filename = 'records.csv'

with open(filename, "w", newline="") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename = 'records_dict.csv'
with open(filename, "w", newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dict)

products = [
    {"sku": 1, "exp_date": 'today', "price": 100},
    {"sku": 2, "exp_date": 'today', "price": 50},
    {"sku": 3, "exp_date": 'tommorow', "price": 200},
    {"sku": 4, "exp_date": 'today', "price": 100.99},
    {"sku": 5, "exp_date": 'tommorow', "price": 500},
    {"sku": 6, "exp_date": 'today', "price": 250},
]

filename = 'records_discount.csv'
list_product = [key for key in products[0]]

with open(filename, "w", newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=list_product, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(products)  # writerows

# newline='' - ominięcie problemu nowej lini
# delimiter=";" - delimiter