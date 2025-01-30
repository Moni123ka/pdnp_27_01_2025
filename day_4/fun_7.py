def connect(**opcje):  # ** dowolna ilość nazwanych
    print(opcje)


connect()  # {} - słownik -> para klucz wartosc
connect(a=10)  # {'a': 10}
connect(a=10, name="Radek")  # {'a': 10, 'name': 'Radek'}


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()  # () {}
all_args(1, 2, 3, 4, 5, 6, 7)  # (1, 2, 3, 4, 5, 6, 7) {}
all_args(a=10, b=34, name="Radek")  # () {'a': 10, 'b': 34, 'name': 'Radek'}
all_args(1, 2, 3, a=10, b=67)  # (1, 2, 3) {'a': 10, 'b': 67}
