n = int(input())  # nombre d'éléments

lst = list(map(int, input().split())) # saisie des valeurs

smallest = min(lst)
largest = max(lst)

res = []
# boucle sur l'intervalle
for val in range(smallest, largest+1):
    s = 0
    for idx in range(n):
        s += (lst[idx]-val)**2   # calcul de la somme des carrés
    res.append(s)  # on ajoute le résultat à la liste

# Juste un print classique, à améliorer peut-être
print(min(res))