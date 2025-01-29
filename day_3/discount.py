from datetime import datetime, date, timedelta

today = date.today()
print("Dzisiejsza data:", today)  # Dzisiejsza data: 2025-01-29
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print("Aktualny czas:", time)  # Aktualny czas: 2025-01-29 13:34:18.474611

print(time.year)  # 2025
print(today.day)  # 29

# tommorow = today + 1 # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
#  days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tommorow = today + timedelta(days=1)
print("Jutro będzie", tommorow)  # Jutro będzie 2025-01-30

formated_data = datetime.now().strftime("%d/%m/%Y")
print(type(formated_data))  # <class 'str'>
print("Data sformatowana:", formated_data)  # Data sformatowana: 29/01/2025

# sformatowany czas 13:40
formated_time = datetime.now().strftime("%H:%M")
print(type(formated_time))  # <class 'str'>
print("Sformatowany czas:", formated_time)  # Sformatowany czas: 13:43

formated_time_usa = datetime.now().strftime("%I:%M %p")
print("Sdformatowany czas 12h:", formated_time_usa)  # Sdformatowany czas 12h: 01:44 PM
