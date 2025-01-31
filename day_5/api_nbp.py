import requests

# pip install requests
url = 'https://api.nbp.pl/api/exchangerates/rates/A/EUR/'

response = requests.get(url)
print(response)  # <Response [200]>
# 2xx 200 ok
# 3xx warningi, przekierowania
# 4xx 404 - brak strony 400 Bad request bledne zapytanie
# 5xx 500 Interenal Server Error - błędy na serwerze

print(response.text)
data = response.json()
print(type(data))
print(data)
# {'table': 'A',
# 'currency': 'euro',
# 'code': 'EUR',
# 'rates': [{'no': '021/A/NBP/2025', 'effectiveDate': '2025-01-31', 'mid': 4.213}]}

print(data['currency'])  # euro
print(data['rates'])
# [
# {'no': '021/A/NBP/2025', 'effectiveDate': '2025-01-31', 'mid': 4.213}
# ]
print(data['rates'][0])  # {'no': '021/A/NBP/2025', 'effectiveDate': '2025-01-31', 'mid': 4.213}
print(data['rates'][0]['mid'])  # 4.213
