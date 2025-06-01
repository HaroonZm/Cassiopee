# Création d'une liste 2D nommée 'l' avec 10 sous-listes, chacune contenant 1001 éléments initialisés à 0
# Cette structure servira à stocker des comptes ou des résultats intermédiaires
l = [[0]*1001 for i in range(10)]

# Initialisation du premier élément de la première sous-liste à 1
# Cela sert de point de départ pour les calculs ultérieurs, indiquant une configuration de base
l[0][0] = 1

# Première boucle : variable 'i' varie de 0 à 100 inclus (101 itérations)
# Elle représente probablement un élément ou une valeur à considérer dans le calcul
for i in range(101): 

    # Deuxième boucle : variable 'j' va de 9 à 1 inclus, en décrémentant de 1 à chaque tour
    # Cela indique qu'on traite les sous-listes 'l[j]' dans l'ordre inverse, sauf la première
    for j in range(9, 0, -1):

        # Troisième boucle : variable 'k' varie de 'i' à 999 inclus
        # Cette boucle parcourt les indices des éléments dans la sous-liste 'l[j]'
        for k in range(i, 1000):

            # Mise à jour de l'élément 'l[j][k]' en y ajoutant la valeur 'l[j-1][k-i]'
            # Cette opération cumule les résultats selon une relation dynamique
            # Elle sert à combiner les calculs précédents pour créer de nouvelles valeurs
            l[j][k] += l[j-1][k-i]

# Boucle infinie qui tourne indéfiniment jusqu'à ce qu'une condition d'arrêt soit rencontrée
while 1:

    # Lecture d'une ligne de l'entrée utilisateur, puis séparation en deux variables 'n' et 'k'
    # 'raw_input()' lit une chaîne de caractères, 'split()' la divise en sous-chaînes,
    # 'map(int, ...)' convertit chacune de ces sous-chaînes en un entier
    n, k = map(int, raw_input().split())

    # Condition d'arrêt : si les deux entrées sont 0, on interrompt la boucle infinie
    # Cela signifie que la fin de l'entrée a été atteinte ou que l'utilisateur souhaite quitter
    if n == k == 0:
        break

    # Affichage de la valeur située à la position [n][k] dans la liste 2D 'l'
    # Cette valeur correspond probablement à un résultat calculé préalablement dans les boucles
    print l[n][k]