#LEGB
# L->LOCAL
# E->ENCLOSING
# G->GLOBAL
# B->BUILT-IN
x = "global x"
def test():
    y = "local y"
    print(y)
    print(x)
test()


