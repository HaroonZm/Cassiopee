n, k = map(int, input().split())
prices = list(map(int, input().split()))  # la liste des prix, je suppose
prices.sort()  # On trie, c'est plus simple comme ça

somme = 0
for idx in range(0, k):  # Attention, faut bien prendre les k premiers
    somme = somme + prices[idx]  # bof, j'aurais pu utiliser += mais bon
# Affichage du résultat
print(somme)