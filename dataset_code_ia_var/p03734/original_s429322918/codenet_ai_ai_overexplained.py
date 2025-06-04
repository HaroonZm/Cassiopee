# Lecture de deux entiers depuis l'entrée standard :
# Le premier entier 'n' représente probablement le nombre total d'objets ou d'éléments disponibles.
# Le second entier 'w' correspond typiquement à une contrainte (par exemple, la capacité maximale de poids d'un sac à dos).
n, w = map(int, input().split())

# Création d'une table pour la programmation dynamique (DP) à 3 dimensions :
# - La première dimension (indice i) représente le nombre d'items considérés jusque-là (de 0 à n).
# - La deuxième dimension (indice j) représente le nombre d'items sélectionnés (de 0 à n).
# - La troisième dimension (indice k) encode une variation de poids possible (de 0 à 4*n), manipulant les différences de poids relatives.
# Chaque cellule est initialisée à -1 pour symboliser une valeur impossible ou non encore atteinte.
dp = [[[-1] * (4 * n) for j in range(n + 1)] for i in range(n + 1)]

# On initialise la situation de départ où :
# - Aucun item n'a été considéré (i = 0)
# - Aucun item n'a été pris (j = 0)
# - Le "poids relatif différentiel" est à 0 (k = 0)
# On assigne la valeur 0 car aucune valeur n'a été accumulée jusque-là.
dp[0][0][0] = 0

# Variable auxiliaire pour stocker le poids du tout premier objet rencontré, qui servira d'étalon pour ajuster les autres poids.
w1 = None

# On parcourt chacun des n objets (numérotés de 0 à n-1) pour lire ses propriétés et mettre à jour la DP.
for i in range(n):
    # Lecture de deux entiers :
    # - 'ws' désigne le poids de l'objet courant.
    # - 'vs' correspond probablement à la valeur/score de cet objet.
    ws, vs = map(int, input().split())
    
    # Si c'est le tout premier objet (i == 0),
    # on sauvegarde son poids dans la variable 'w1' pour référence ultérieure.
    if i == 0:
        w1 = ws

    # Mise à jour du poids de l'objet courant pour qu'il devienne relatif au poids du premier objet.
    # Ainsi, tous les poids sont exprimés comme un écart par rapport à w1.
    ws -= w1

    # On considère tous les cas possibles où on aurait sélectionné 'j' objets parmi les i+1 objets (j va de 0 à i+1 inclus).
    for j in range(i + 2):
        # On parcourt toutes les variations possibles de la somme relative des poids (k).
        for k in range(4 * n):
            # Assurer que l'on ne tente pas de retirer un objet alors qu'on en a sélectionné aucun (j-1 >= 0).
            # On vérifie également qu'on ne dépasse pas de manière négative la borne de la somme relative des poids (k-ws >= 0).
            # Enfin, on s'assure que le précédent état est atteignable (dp[i][j-1][k-ws] >= 0).
            if j - 1 >= 0 and k - ws >= 0 and dp[i][j - 1][k - ws] >= 0:
                # Si on décide de sélectionner l'objet courant :
                # - Soit on ne sélectionne pas l'objet à ce tour et conserve la meilleure valeur précédente : dp[i][j][k]
                # - Soit on inclut l'objet (d'où +vs) et on récupère la meilleure solution à l'étape d'avant (pour j-1, k-ws)
                # On prend la meilleure des deux options.
                dp[i + 1][j][k] = max(dp[i][j][k], dp[i][j - 1][k - ws] + vs)
            else:
                # Si on ne sélectionne pas l'objet, la meilleure solution est simplement celle de l'état sans cet objet.
                dp[i + 1][j][k] = dp[i][j][k]

# Initialisation de la variable 'ans' pour stocker la meilleure valeur totale atteinte qui respecte les contraintes de poids.
ans = 0

# On parcourt toutes les combinaisons possibles de nombre d'items sélectionnés (j) et de variation finale de poids (k).
for j in range(n + 1):
    for k in range(4 * n):
        # On recalcule le poids total réel pour chaque situation :
        # - Il correspond à la somme du poids de base (w1) multiplié par le nombre d'objets sélectionnés (j)
        #   auquel on ajoute l'écart de poids cumulé (k).
        # On vérifie si ce poids total n'excède pas la capacité maximale autorisée (w).
        if w1 * j + k <= w:
            # Si la solution en cours est valide et meilleure que la précédente, on la retient.
            ans = max(ans, dp[-1][j][k])

# On affiche la meilleure valeur trouvée respectant la contrainte de poids.
print(ans)