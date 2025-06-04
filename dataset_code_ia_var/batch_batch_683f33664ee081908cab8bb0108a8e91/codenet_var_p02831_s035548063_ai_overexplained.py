# Demander à l'utilisateur de saisir deux entiers séparés par un espace sur une seule ligne
# La fonction input() lit la saisie utilisateur sous forme de chaîne de caractères
# La méthode split() divise la chaîne en une liste de sous-chaînes là où il y a des espaces
# La fonction map() applique la fonction int() à chaque élément de la liste (chaque sous-chaîne devient un entier)
# Les deux entiers résultants sont affectés respectivement aux variables A et B
A, B = map(int, input().split())

# Initialiser une variable n avec la valeur 1
# Cela servira pour multiplier A par différents entiers consécutifs
n = 1

# Démarrer une boucle infinie avec while True pour rechercher le résultat désiré
while True:
    # Multiplier la valeur de A par n, stocker le résultat dans la variable A_
    # Le caractère de soulignement (_) est fréquemment utilisé pour distinguer une variable temporaire
    A_ = A * n

    # Calculer le reste de la division de A_ par B à l'aide de l'opérateur modulo (%)
    # Si ce reste est égal à 0, cela signifie que A_ est un multiple de B
    if A_ % B == 0:
        # Afficher la valeur de A_ sur la sortie standard (typiquement l'écran)
        print(A_)
        # Arrêter immédiatement l'exécution du programme en appelant la fonction exit()
        # Cela termine le script même si d'autres instructions suivent après la boucle
        exit()
    
    # Si le reste n'est pas nul, augmenter la valeur de n de 1 avec n += 1
    # Cela permet de vérifier le prochain multiple de A à l'itération suivante
    n += 1