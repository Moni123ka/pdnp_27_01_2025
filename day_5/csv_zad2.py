import csv

# filename = 'records.csv'
filename = 'records_discount.csv'

fields = []
rows = []

with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)
    csv_f.seek(0)  # powrót odczytu na początek pliku
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)
    # csvreader = csv.reader(csv_f, delimiter=";")
    print(csvreader)  # <_csv.reader object at 0x000002B1FA67E6E0>

    fields = next(csvreader)  # pobierz eleemnt i ustaw na następny
    for row in csvreader:  # wystartuje od drugiego wiersza
        # print(row)
        rows.append(row)

print("Fields:", fields)  # Fields: ['name', 'branch', 'year', 'cgpa']
print("Rows:", rows)  # Rows: [['radek', 'coe', '3', '0']]
