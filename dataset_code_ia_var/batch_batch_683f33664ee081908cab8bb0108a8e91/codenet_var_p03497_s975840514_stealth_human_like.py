# Bon, ok, on va faire ça différemment, plus “humain”
n, k = map(int, input().split())
a = list(map(int, input().split()))

counter = {}
for el in a:
    if el in counter:
        counter[el] += 1
    else: # première fois qu'on voit el
        counter[el] = 1

res = 0
used = 0
# Je trie, mais je galère un peu avec la syntaxe lambda...
lst = sorted(counter.items(), key=lambda item: -item[1])
for tup in lst:
    if used >= k:
        res += tup[1]  # On ajoute les extras
    else:
        used = used + 1   # On change juste le compteur, on fait rien d'autre (normal)

print(res)  # voilà !