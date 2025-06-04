n = int(input())
a = list(map(int, input().split()))
ans = 10000000  # assez grand normalement
somme = 0

for idx in range(n):
    somme = somme + a[idx] # on ajoute, classique
    # Est-ce que c'est la meilleure façon ? Peut-être
    moyenne = somme // (idx + 1)
    # on essaie de garder la plus petite valeur trouvée
    if moyenne < ans:
        ans = moyenne
print(ans)