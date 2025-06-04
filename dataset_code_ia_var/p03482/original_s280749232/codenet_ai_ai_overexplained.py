# Demande à l'utilisateur de saisir une chaîne de caractères et supprime les espaces éventuels en début et fin de chaîne
s = input().strip()

# Calcule la longueur de la chaîne de caractères entrée par l'utilisateur
n = len(s)

# Initialise deux variables pour stocker les réponses minimales pour les caractères '1' et '0'
# On les initialise à la longueur de la chaîne, ce qui garantit que toute valeur trouvée sera plus petite
ansone = n  # Stockera la valeur minimale calculée pour '1'
anszero = n  # Stockera la valeur minimale calculée pour '0'

# Parcours de chaque caractère de la chaîne de caractères
# La fonction enumerate(s) retourne à chaque itération l'index 'i' et le caractère 'c' situés à cette position
for i, c in enumerate(s):
    # Calcule la distance entre le caractère courant et le début de la chaîne
    ld = i  # left distance (distance à gauche)
    # Calcule la distance entre le caractère courant et la fin de la chaîne
    rd = n - i - 1  # right distance (distance à droite)
    
    # Vérifie si le caractère courant est le caractère '1'
    if c == '1':
        # Met à jour la variable 'ansone' avec la valeur minimale entre sa valeur actuelle et la plus grande distance (gauche ou droite)
        # L'utilisation de max(ld, rd) signifie que l'on cherche la plus grande distance jusqu'aux extrémités pour conserver l'intégrité d'un groupe de '1'
        ansone = min(ansone, max(ld, rd))
    else:
        # Si ce n'est pas un '1', alors on considère que c'est un '0'
        # On fait la même opération mais pour la variable 'anszero'
        anszero = min(anszero, max(ld, rd))

# Après avoir parcouru toute la chaîne et mis à jour les variables ansone et anszero,
# on utilise la fonction max pour afficher la plus grande des deux valeurs
# Ceci représente, parmi les deux valeurs minimales trouvées pour '1' et '0', la plus grande
print(max(ansone, anszero))