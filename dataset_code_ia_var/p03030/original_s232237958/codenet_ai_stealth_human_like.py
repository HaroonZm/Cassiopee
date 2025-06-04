N = int(input())
results = []
# J'utilise une liste pour stocker les trucs
for i in range(N):
    s, p = input().split()
    results.append([s, int(p)])  # ajouter les paires (je garde ça comme des listes... c'est pratique)

copy_results = results[:]  # petit raccourci pour copier
copy_results.sort(key=lambda x: (x[0], -x[1]))  # tri chelou, mais ça marche normalement

# Affichage (ça imprime l'indice d'apparition dans la liste originale)
for elem in copy_results:
    idx = results.index(elem)  # bon, tant pis pour les doublons, c'est pas optimisé mais ça passe
    print(idx + 1)  # 1-based index, attention!