# funkcja wewnętrzna, zagnieżdzona
# dekorator wykorzystuje zasadę funkcji wew
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    # return fun2()  # zwraca wynik funkcji
    return fun2  # zwraca adres funkcji (referencje)


fun1()  # To jest fun1
xFun = fun1()  # do zmiennej xFun wrzucamy wynik działania fun1 -> adres funkcji fun2
print(type(xFun))  # <class 'function'>
print(xFun)  # <function fun1.<locals>.fun2 at 0x000002BFFD918AE0>
xFun()  # To jest fun2
xFun()
print("Inne rzeczy")
xFun()
# To jest fun1
# To jest fun1
# <class 'function'>
# <function fun1.<locals>.fun2 at 0x000001AC06698AE0>
# To jest fun2
# To jest fun2
# Inne rzeczy
# To jest fun2
