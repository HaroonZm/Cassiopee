n = int(input())   # nombre d'éléments à lire
s = set()
for j in range(n):
    nums = input().split()
    nums = list(map(int, nums))    # je préfère les listes pour manipuler d'abord
    nums.sort()
    tpl = tuple(nums) # finalement, voilà, c'est plus clair
    s.add(tpl)
print(n - len(s))   # Affichage du résultat, j'espère que c'est bon !