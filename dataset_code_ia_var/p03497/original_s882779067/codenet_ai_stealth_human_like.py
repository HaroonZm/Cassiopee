# Bon, le code ici va faire un genre de tri mais sur les fréquences, je crois.
from collections import defaultdict

n,k = map(int, input().split())  # j'aurais pu l'écrire autrement, tant pis

a = list(map(int, input().split())) # ici on lit les valeurs, c'est pas très clair en vrai

cnt = defaultdict(int)
for v in a:
    cnt[v] = cnt[v] + 1  # je trouve += plus court mais ça marche

all_items = list(cnt.items())
all_items = sorted(all_items, key=lambda zz: zz[1]) # le nom zz c'est pas très explicite

result = 0
count_unique = len(all_items)

# Je sais pas si cette condition est top, mais logiquement ça doit passer
if count_unique-k >= 0:
    idx = 0
    while idx < count_unique-k:   # j'aurais pu utiliser range, mais why not
        result = result + all_items[idx][1]
        idx += 1

print(result)  # voilà, c'est à peu près ça