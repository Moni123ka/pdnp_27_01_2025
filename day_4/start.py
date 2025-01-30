# import fun_2
#
# print(fun_2.oblicz_vat(5000))  # 6150.0
import pakiet

print(15 * "-")  # ---------------

# po dodaniu w pliku __init__.py
# __all__ = ['powitanie']
# metoda z pakietu działa
pakiet.powitanie()

# import bezposrednio pliku z pakietu
from pakiet import fun

fun.info()  # Jestem pakietem
fun.powitanie()

# import pliku z pakietu jako alias
import pakiet.fun as pk

pk.info()
pk.powitanie()
# ---------------
# Cześć
# Jestem pakietem
# Cześć
# Jestem pakietem
# Cześć
