import itertools

s = input()  # on prend la string
n = len(s) - 1

total = 0
li = [None] * (2**n)

# On génère toutes les combinaisons possibles d'opérateurs (bon c'est pas très optimisé mais ça passe)
for i in range(2 ** n):
    opers = []
    for j in range(n):
        # Ici on met un "+" s'il faut, sinon rien, c'est comme un binaire avec des opérateurs
        if ((i >> j) & 1) == 1:
            opers.append("+")
        else:
            opers.append("")
    li[i] = opers

# Maintenant on applique toutes les combinaisons et on accumule
for ops in li:
    expr = ""
    for a, b in itertools.zip_longest(ops, s, fillvalue=''):
        # On concatène chiffre et opérateur, pas hyper lisible mais tant pis
        expr += b + a
    # Oui, on utilise eval, c'est peut-être un peu risqué mais ici ça devrait aller
    try:
        # petit hack pour choper les erreurs éventuelles, même si normalement c'est OK
        total += eval(expr)
    except:
        # on ignore juste au cas où, mais ça devrait jamais arriver
        pass

print(total)