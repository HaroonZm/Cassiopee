# Demande à l'utilisateur de saisir une chaîne de caractères et affecte cette valeur à la variable T.
# La fonction input() lit une ligne d'entrée depuis le clavier, retourne une chaîne.
T = input()

# Demande à l'utilisateur de saisir une deuxième chaîne de caractères, affectée à la variable P.
P = input()

# Calcule la longueur de la chaîne T (le nombre de caractères dans T).
# La fonction len() retourne un entier correspondant au nombre d'éléments d'une séquence.
t = len(T)

# Calcule la longueur de la chaîne P, puis affecte cette valeur à la variable p.
p = len(P)

# Démarre une boucle for. La fonction range() génère une séquence d'entiers, ici démarrant à 0
# et allant jusqu'à (t - p), inclus, afin de parcourir toutes les positions possibles où P
# peut apparaître entièrement dans T sans dépasser la longueur de T.
# t - p + 1 donne le nombre total de positions de départ possibles afin que la sous-chaîne
# extraite ait la même longueur que P.
for i in range(t - p + 1):
    # Extrait de la chaîne T une sous-chaîne débutant à l'index i et s'arrêtant à l'index i + p (exclu).
    # T[i : i + p] utilise la notation de tranchage (slicing) en Python pour obtenir un segment de la chaîne.
    # Compare la sous-chaîne obtenue avec la chaîne P à l'aide de l'opérateur d'égalité ==
    # Si elles sont strictement identiques caractère par caractère, la condition est vraie.
    if T[i : i + p] == P:
        # Affiche la valeur actuelle de i, qui correspond à l'indice où la sous-chaîne P commence dans T.
        # La fonction print() affiche la valeur dans le terminal suivie d'un retour à la ligne.
        print(i)