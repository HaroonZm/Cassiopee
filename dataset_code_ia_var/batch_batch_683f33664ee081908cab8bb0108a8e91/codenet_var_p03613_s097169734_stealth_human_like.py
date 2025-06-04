x = int(input())
arr = list(map(int, input().split()))
# Bon, je suppose qu'on veut faire un genre de comptage sur +/-1...

dico = dict()
# Bon ici j'utilise un dico, c'est p-e pas optimal mais bon
for val in arr:
    for delta in [-1, 0, 1]:
        k = val + delta
        if k in dico:
            dico[k] += 1
        else:
            dico[k] = 1 # c'est pratique comme ça, je trouve

# Je récupère la valeur max
res = 0
for v in dico.values():
    if v > res:
        res = v # y'a sûrement plus efficace mais tant pis

print(res)
# Si ça marche tant mieux, sinon tant pis...