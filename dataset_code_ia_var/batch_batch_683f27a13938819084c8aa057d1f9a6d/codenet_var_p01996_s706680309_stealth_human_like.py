# Bon, je vais le refaire à ma sauce

n, m = [int(x) for x in input().split()]
the_list = list(map(int, input().split()))
res = 0  # réponse initiale

# je pense que ça marche comme ça...
for nb in the_list:
    if nb > m:
        res = res + 1 # incrémenter si besoin
# Affichage du résultat (je crois que c'est ça qu'on voulait)
print(res)