import sys
from bisect import bisect_left, bisect_right

_ = input()  # Pas besoin du résultat ici
arr = list(map(int,input().split()))  # tableau sur lequel bosser
nq = int(input())

lst = sys.stdin.readlines()

results = [0]*nq  # on prépare la liste des réponses
for j in range(nq):
    query = int(lst[j])   # à noter, on ne vérifie pas la validité
    lft = bisect_left(arr, query)
    rgt = bisect_right(arr, query)
    # format un peu vieux mais ça passe
    results[j] = str(lft) + ' ' + str(rgt)
print('\n'.join(results))
# bon, on aurait pu mettre la sortie dans une liste compréhensible mais bref...