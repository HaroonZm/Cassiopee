# On commence par demander à l'utilisateur de rentrer deux entiers, séparés par un espace
# La fonction input() lit une ligne depuis l'entrée standard (clavier)
# La méthode split() sépare cette ligne en une liste de chaînes (par défaut, séparées par des espaces)
# La fonction map applique la fonction int à chaque élément de cette liste pour les convertir en entiers
# Enfin, on affecte ces deux entiers respectivement à N et M
N, M = map(int, input().split())

# On initialise une chaîne de caractères vide qui servira à stocker les données de la première table
# Une chaîne vide est désignée par deux guillemets simples sans texte entre eux : ''
table1 = ''

# On initialise une deuxième chaîne de caractères vide pour la deuxième table
table2 = ''

# On commence une boucle qui s'exécutera 2*N fois (de 0 à 2*N-1)
# range(2*N) crée un itérable contenant les entiers de 0 à 2*N-1 inclus
for i in range(2 * N):
    # Si l'indice courant i est strictement inférieur à N
    # Cela signifie que nous traitons encore les N premières lignes à affecter à table1
    if i < N:
        # La fonction input() lit la ligne suivante depuis l'entrée
        # On ajoute (concatène) cette ligne à table1 à l'aide de l'opérateur +=
        table1 += input()
    else:
        # Sinon, si i >= N, nous sommes sur les N dernières lignes, qui doivent aller dans table2
        # On lit la ligne courante avec input() et on ajoute son contenu à table2
        table2 += input()
        
# Après la boucle, les deux chaînes table1 et table2 contiennent chacune N * M caractères

# On initialise une variable count à 0
# Cette variable servira à compter le nombre de positions où les caractères dans les deux tables diffèrent
count = 0

# zip(table1, table2) crée un itérable de tuples, où chaque tuple contient un caractère de table1 et un caractère de table2, à la même position
# enumerate n'est pas utilisé ici car l'indice n'est pas nécessaire
for i, j in zip(table1, table2):
    # Pour chaque paire de caractères (i, j), on vérifie s'ils sont différents
    # L'opérateur != teste l'inégalité
    if i != j:
        # Si c'est le cas, on incrémente count de 1 avec l'opérateur +=
        count += 1

# Enfin, on affiche la valeur finale de count à l'aide de la fonction print()
# Cela correspond au nombre de différences entre table1 et table2
print(count)