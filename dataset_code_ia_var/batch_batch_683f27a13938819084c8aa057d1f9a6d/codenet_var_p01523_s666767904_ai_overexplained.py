# Demande à l'utilisateur d'entrer deux entiers séparés par un espace
# Utilise la fonction input() pour lire une ligne de texte depuis l'entrée standard (typiquement le clavier)
# Utilise la fonction split() pour séparer la chaîne en une liste de sous-chaînes en se basant sur les espaces
# Utilise map(int, ...) pour convertir chaque sous-chaîne en entier
# Décompose le résultat en deux variables n et m
n, m = map(int, input().split())

# Initialise une liste pour stocker les intervalles/propositions
# Pour chaque nombre de lignes (m) :
#   - Lit une ligne de l'entrée standard, la sépare en parties, convertit chaque élément en entier, et forme une sous-liste [a, b]
#   - Utilise la compréhension de liste pour faire cela en une ligne
# Trie la liste résultante, de sorte que les intervalles sont classés par leur début (puis éventuellement par leur fin)
pros = sorted([list(map(int, input().split())) for _ in range(m)])

# Initialise un index à 0, qui servira à parcourir les éléments de 'pros' un par un
index = 0

# Initialise la variable 'covered' à 0 ; elle gardera la trace du point jusqu'où l'on a couvert la plage de 1 à n (inclus)
covered = 0

# Initialise la variable 'right' à 0 ; elle gardera la trace du point le plus à droite que l'on peut atteindre avec les intervalles sélectionnés jusqu'à présent
right = 0

# Initialise le compteur de la réponse à 0 ; il comptera le nombre d'intervalles sélectionnés pour couvrir toute la plage
ans = 0

# Utilise une boucle infinie, 'while True', qui ne se stoppe que lorsqu'on rencontre une instruction 'break'
while True:
    # Récupère le début 'a' et la fin 'b' du 'index'-ième intervalle dans la liste 'pros'
    a, b = pros[index]

    # Condition 1 : S'il y a un trou dans la couverture, c'est-à-dire si le début de l'intervalle courant 'a' est supérieur à 'covered + 1'
    if a > covered + 1:
        # Vérifie si on vient d'essayer d'étendre la couverture mais qu'aucune extension n'est trouvée ('covered == right')
        if covered == right:
            # Si c'est le cas, cela signifie qu'il y a une partie non couverte et qu'il est impossible de tout couvrir
            print("Impossible")
            # Sort de la boucle, et donc du programme principal
            break

        # Sinon, met à jour la borne couverte ('covered') jusqu'à la meilleure extension atteignable actuellement ('right')
        covered = right
        # Incrémente le compteur du nombre d'intervalles utilisés, car l'on sélectionne un intervalle pour couvrir jusqu'à 'right'
        ans += 1
        # Utilise 'continue' pour retourner au début de la boucle et refaire une itération avec l'intervalle actuel (sans avancer 'index')
        continue
    else:
        # Sinon, si l'intervalle courant commence dans la zone à couvrir, on essaye au moins de l'étendre au maximum vers la droite
        # Prend le maximum entre le 'right' courant et la fin de l'intervalle actuel 'b' pour couvrir le plus loin possible
        right = max(right, b)
        # Passe à l'intervalle suivant en incrémentant l'index
        index += 1

    # Vérifie si toute la plage jusqu'à n est couverte ('covered == n')
    if covered == n:
        # Si tel est le cas, affiche le nombre minimal d'intervalles nécessaires pour couvrir toute la plage
        print(ans)
        # Sort de la boucle principale
        break

    # Vérifie si tous les intervalles ont été parcourus ('index == m')
    if index == m:
        # Si c'est le cas, il faut sélectionner le dernier ensemble d'intervalles possibles pour couvrir le plus loin possible
        covered = right
        # Incrémente le compteur d'intervalles utilisés
        ans += 1
        # Affiche la réponse finale si toute la plage est couverte, sinon affiche "Impossible"
        print(ans if covered == n else "Impossible")
        # Sort de la boucle
        break