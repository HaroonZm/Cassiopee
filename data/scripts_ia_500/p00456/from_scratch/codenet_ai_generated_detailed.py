# On commence par lire les scores des participants des deux universités.
# Ensuite, on trie les listes de scores décroissantement.
# On somme les 3 meilleurs scores de chaque université.
# Enfin, on affiche ces sommes séparées par un espace.

# Lecture des scores de W大学 (10 participants)
w_scores = [int(input()) for _ in range(10)]

# Lecture des scores de K大学 (10 participants)
k_scores = [int(input()) for _ in range(10)]

# Tri décroissant des scores pour avoir les meilleurs en premier
w_scores.sort(reverse=True)
k_scores.sort(reverse=True)

# Somme des 3 meilleurs scores pour chaque université
w_total = sum(w_scores[:3])
k_total = sum(k_scores[:3])

# Affichage des résultats
print(w_total, k_total)