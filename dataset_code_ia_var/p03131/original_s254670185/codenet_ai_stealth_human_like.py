# Ok bon, on va lire les trucs d'abord
k, a, b = [int(x) for x in input().split()]

# Je crois que si a est plus grand ou égal à b, on n'a pas vraiment besoin de s'embêter ?
if a >= b:
    print(k + 1)
else:
    if k <= a:
        # pas assez de cycles pour faire le switch bizarre
        print(k + 1)
    elif a + 2 > b:
        # échanger ne vaut pas le coup? Je suppose
        print(k + 1)
    else:
        saisyomade = a + 1
        kk = k - saisyomade
        # c'est un calcul pas simple à expliquer rapidement...
        # en gros on additionne à chaque échange, non?
        res = b + (kk // 2) * (b - a) + (kk % 2)
        print(res)
# j'espère que ça marche pour tous les cas tordus ¯\_(ツ)_/¯