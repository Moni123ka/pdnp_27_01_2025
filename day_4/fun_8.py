def all_params(a, b, /, c=42, d=256):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")


all_params(1, 2)  # a=1, b=2
all_params(1, 2, 3, 4)  # a=1, b=2
all_params(1, 2, c=3, d=4)  # a=1, b=2
# a=1, b=2
# c=42, d=256
# a=1, b=2
# c=3, d=4
# a=1, b=2
# c=3, d=4
# TypeError: all_params() got some positional-only arguments passed as keyword arguments: 'a, b'
# (a, b, /,c=42, d=256)
# / odziela pozycyjne od nazwanych
# a i b w tym przypadku obowiązkowa muszą byc przekazane jako pozycyjne
# all_params(a=10, b=90)
all_params(10, 90)  # c=42, d=256

print(10 * "-")


def all_params2(a, b, /, c=42, *args, d=256, **kwargs):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")
    print(f"{args=}")
    print(f"{kwargs=}")


# *args - dowolna ilosć argumentów pozycyjnych
all_params2(1, 2)  # a=1, b=2
all_params2(1, 2, 3)  # a=1, b=2, c=3, d=256
all_params2(1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5)  # args=(4, 5, 5, 5, 5, 5, 5, 5)
all_params2(1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, d=100)
# c=3, d=100
# args=(4, 5, 5, 5, 5, 5, 5, 5)
# po args następny musi być przekazany po nazwie
all_params2(1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, d=100, name="radek")
# a=1, b=2
# c=3, d=100
# args=(4, 5, 5, 5, 5, 5, 5, 5)
# kwargs={'name': 'radek'}
# ze względu na / a=45 trafi do kwargs
all_params2(1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, f=56, name="radek", a=45)
# a=1, b=2
# c=3, d=256
# args=(4, 5, 5, 5, 5, 5, 5, 5)
# kwargs={'f': 56, 'name': 'radek', 'a': 45}
