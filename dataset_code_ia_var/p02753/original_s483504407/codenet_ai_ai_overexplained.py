# Demande à l'utilisateur de saisir une chaîne de caractères et stocke la saisie dans la variable S
S = input()

# Initialise une liste L avec deux entiers, tous les deux à 0
# L[0] servira à compter le nombre de fois où "A" apparaît
# L[1] servira à compter le nombre de fois où tout autre caractère apparaît
L = [0, 0]

# Utilise une boucle for pour répéter les instructions à l'intérieur du bloc 3 fois
# La fonction range(3) génère une séquence des entiers : 0, 1, 2 (donc 3 valeurs, pour S[0], S[1], S[2])
for i in range(3):
    # Vérifie si le caractère à la position i dans la chaîne S est exactement "A"
    if S[i] == "A":
        # Si c'est le cas, incrémente la valeur à l'index 0 de la liste L de 1
        # Cela augmente le compteur du nombre de "A" rencontrés jusque là
        L[0] += 1
    else:
        # Si le caractère n'est pas "A", incrémente la valeur à l'index 1 de L de 1
        # Cela augmente le compteur du nombre de caractères différents de "A"
        L[1] += 1

# Utilise la fonction max pour obtenir la plus grande valeur dans la liste L (soit le nombre maximum de "A", soit d'autres caractères)
if max(L) == 3:
    # Cela signifie que tous les caractères sont les mêmes : soit tous "A", soit tous autres
    # Dans ce cas, affiche la chaîne de caractères "No" à l'écran
    print("No")
else:
    # Sinon, cela veut dire qu'il y a au moins deux types de caractères différents parmi les trois (tous ne sont pas identiques)
    # Dans ce cas, affiche la chaîne de caractères "Yes"
    print("Yes")