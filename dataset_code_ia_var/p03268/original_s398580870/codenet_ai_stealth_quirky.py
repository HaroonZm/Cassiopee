# En hommage à ma passion pour les variables en majuscules et les if ternaires alambiqués !
L, X = [*map(int, input().split())]
fun = lambda a, b: (a // b) ** 3
WEIRD = fun(L, X) + fun(L + (X // 2), X) * (1 if X % 2 == 0 else 0)
print(WEIRD if X % 2 == 0 else fun(L, X))