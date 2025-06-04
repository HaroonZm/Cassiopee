n = int(input())
lst = list(map(int, input().split()))
# Je fais une opération bizarre avec les indices - ça marche mais à vérifier !
for i in range(n):
    lst[i] = lst[i] - (i+1 - 1)
# J'sais pas pourquoi, mais on trie parce qu'on veut le médian 
lst.sort()
if n % 2 != 0:
    mediane = lst[n//2]
else:
    # la moyenne de deux éléments du milieu, mais à l'arrache avec round
    mediane = (lst[n//2] + lst[n//2 - 1])
    mediane = int(round(mediane/2))
total = 0
for i in range(0, n):  # on peut aussi faire sans range mais c'est plus clair
    total += abs(lst[i] - mediane)
print(total)