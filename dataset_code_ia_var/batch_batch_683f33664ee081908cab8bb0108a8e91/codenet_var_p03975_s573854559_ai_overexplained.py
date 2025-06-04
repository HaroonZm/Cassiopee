# Demande à l'utilisateur de saisir trois valeurs séparées par des espaces
# Ces valeurs seront lues sous forme de chaîne de caractères à partir de l'entrée standard (clavier)
# La fonction input() lit toutes les valeurs saisies jusqu'à la touche "Entrée"
# La méthode split() découpe la chaîne en une liste de sous-chaînes, en utilisant l'espace comme séparateur par défaut
# La fonction map(int, ...) applique la fonction int() à chaque sous-chaîne pour la convertir en entier
# Enfin, les trois entiers obtenus sont affectés respectivement aux variables N, A et B
N, A, B = map(int, input().split())

# Initialise une variable r à 0
# Cette variable servira de compteur pour le nombre d'éléments ne respectant pas la condition
r = 0

# Crée une boucle qui va s'exécuter N fois, où N est le nombre entier saisit précédemment
# La fonction range(N) génère une séquence de nombres entiers allant de 0 à N-1
# La variable i va donc prendre successivement les valeurs 0, 1, ..., N-1 pour chaque itération de la boucle
for i in range(N):
    # À chaque itération de la boucle, l'utilisateur doit saisir une valeur (nombre entier)
    # La fonction input() permet de lire cette valeur depuis l'entrée standard
    # La fonction int() convertit la chaîne obtenue en un entier
    t = int(input())
    
    # Vérifie si la valeur t n'appartient pas à l'intervalle [A, B)
    # L'expression "A <= t < B" teste si t est supérieur ou égal à A ET strictement inférieur à B
    # L'opérateur "not" inverse le résultat du test : il sera vrai si t < A ou t >= B
    if not A <= t < B:
        # Si la condition précédente est vraie, on entre dans ce bloc
        # On incrémente la variable r de 1, ce qui revient à compter le nombre de valeurs ne respectant pas l'intervalle
        r += 1

# Après l'exécution de la boucle, la variable r contient le nombre total d'entiers qui ne sont pas dans [A,B)
# Affiche la valeur de r dans la sortie standard
print(r)