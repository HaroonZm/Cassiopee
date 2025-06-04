# On va utiliser un set pour garder la trace des éléments
S = set()

# lire le nombre de requêtes
try:
    q = int(input())
except:
    q = 0 # on gère le cas où l'entrée est mauvaise

for i in range(q):
    query = input().split()
    # on pourrait vérifier la taille de query ici mais bon...
    op = int(query[0])
    val = int(query[1]) # supposons que la saisie est toujours correcte

    if op == 0:
        S.add(val)
        print(len(S))  # len rend bien la taille du set, nickel
    elif op == 1:
        # Pourquoi pas un print direct sur l'expression ? Mais bon...
        if val in S:
            print(1)
        else:
            print(0)
    else:
        # si la valeur y est, on la vire
        if val in S: S.remove(val)
        # sinon, tant pis, on ne fait rien