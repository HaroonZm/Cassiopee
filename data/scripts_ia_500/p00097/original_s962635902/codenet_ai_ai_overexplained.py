# Déclaration d'une variable nommée 'm' et affectation de la valeur entière 1001
# Cette variable 'm' sera utilisée comme taille maximale pour des listes internes
m = 1001

# Déclaration d'une variable 'A' qui est un objet range allant de 0 à 8 inclus (9 éléments au total)
# 'A' représente un ensemble de nombres allant de 0 à 8, utilisé pour les indices dans les boucles
A = range(9)

# Création d'une liste à deux dimensions (liste de listes) nommée 'd'
# Pour chaque élément 'i' dans A (donc 9 fois), on crée une liste de 1001 zéros
# On obtient ainsi une matrice de 9 lignes et 1001 colonnes, initialisée à zéro
d = [[0] * m for i in A]

# Une boucle for qui itère 101 fois, avec la variable 'i' allant de 0 à 100 inclus
for i in range(101):
    # Une boucle for sur 'j' qui parcourt la liste A dans l'ordre inverse (de 8 à 0)
    for j in A[::-1]:
        # Si 'j' vaut 0, on assigne 1 à la case d[j][i]
        # Cela signifie que pour la ligne 0 et la colonne i, la valeur est 1
        # Ceci initialise la première ligne avec 1 jusqu'à l'indice 100 inclus
        if j == 0:
            d[j][i] = 1
        else:
            # Sinon (j > 0), on effectue une autre boucle sur 'k' de 0 jusqu'à m - i (exclus)
            for k in range(m - i):
                # On ajoute à la valeur d[j][k + i] la valeur d[j-1][k]
                # C'est une opération de cumul qui combine les valeurs de la ligne précédente avec un décalage
                d[j][k + i] += d[j - 1][k]

# Une boucle infinie 'while 1' qui continue indéfiniment jusqu'à une interruption manuelle ou break
while 1:
    # Utilisation de la fonction 'raw_input()' pour lire une ligne d'entrée utilisateur
    # Ensuite, on sépare cette chaîne par les espaces et on convertit chacune des deux valeurs en entier
    n, s = map(int, raw_input().split())
    
    # Condition d'arrêt : si les deux valeurs saisies 'n' et 's' sont toutes deux égales à 0
    # Alors on interrompt la boucle infinie avec l'instruction 'break'
    if n == s == 0:
        break
    
    # Affichage de la valeur disons issue de la matrice 'd' à la ligne n-1 et colonne s
    # Note : on fait n-1 parce que la ligne 0 correspond à n=1 dans le contexte
    print d[n - 1][s]