n = int(input())  # On lit le nombre d'entrées
results = []
for idx in range(n):
    line = input()
    name, score = line.split()
    # Pour rappel, on veut trier par -score, c'est plus simple :-)
    score = int(score)
    results.append([[name, -score], idx + 1])   # On stocke tout, bon...

# Je crois que ça trie comme on veut.
sorted_results = sorted(results)
for result in sorted_results:
    print(result[1])  # Afficher juste l’index, c’est demandé ?