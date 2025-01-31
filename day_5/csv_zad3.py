import pandas

# pip install pandas

# data = pandas.read_csv('records.csv')
data = pandas.read_csv('records_discount.csv', delimiter=";")

print(data)
#    sku  exp_date   price
# 0    1     today  100.00
# 1    2     today   50.00
# 2    3  tommorow  200.00
# 3    4     today  100.99
# 4    5  tommorow  500.00
# 5    6     today  250.00

print(data.columns) # Index(['sku', 'exp_date', 'price'], dtype='object')
print(data.values)
# [[1 'today' 100.0]
#  [2 'today' 50.0]
#  [3 'tommorow' 200.0]
#  [4 'today' 100.99]
#  [5 'tommorow' 500.0]
#  [6 'today' 250.0]]
print(data.items)
# <bound method DataFrame.items of    sku  exp_date   price
# 0    1     today  100.00
# 1    2     today   50.00
# 2    3  tommorow  200.00
# 3    4     today  100.99
# 4    5  tommorow  500.00
# 5    6     today  250.00>