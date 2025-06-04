# hmm... je crois que je dois additionner les K plus petits éléments
N, K = map(int, input().split())
l = list(map(int, input().split()))
somme = 0
for loop in range(K):
    m = min(l)      # je prends le plus petit a chaque tour
    somme = somme + m
    l.remove(m)     # j'enlève direct, ça marche je crois
print(somme) # on affiche le résultat (normalement ça marche)