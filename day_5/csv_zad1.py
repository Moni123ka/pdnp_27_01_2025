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

