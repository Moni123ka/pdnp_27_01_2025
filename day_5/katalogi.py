import shutil
from pathlib import Path

base_path = Path('ops_example')
base_path2 = Path('ops_example/D')

print(base_path)
print(base_path2)
# ops_example
# ops_example\D

if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)

base_path.mkdir()  # tworzenie katalogu

path_b = base_path / 'A' / 'B'
path_c = base_path / 'A' / 'C'
path_d = base_path / 'A' / 'D'

# path_b.mkdir() # FileNotFoundError: [WinError 3] The system cannot find the path specified: 'ops_example\\A\\B'
# niema katalogu A, nie potrafi stworzyć  A i B w ten sposób
path_b.mkdir(parents=True)  # wskazanie by tworzył cała ściezke z podkatalogami
path_c.mkdir()  # zadziałą bo już kaatalog A istnieje

for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, 'w', encoding='utf-8') as stream:
        stream.write(f"Jakas treść pliku {filename}")

# przeniesienie katalogu
shutil.move(path_b, path_d)
ex1 = path_d / 'ex1.txt'
ex1.rename(ex1.parent / 'ext1renamed.log')

ex1 = path_d / 'ext1renamed.log'
docelowy = path_c
# shutil.copy(ex1, docelowy)
shutil.move(ex1, docelowy)
