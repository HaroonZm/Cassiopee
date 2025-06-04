# Création d'une liste appelée 'dp' ("dynamic programming") utilisée pour stocker les résultats intermédiaires.
# Cette liste aura une taille de 301 (pour les indices de 0 à 300 inclus).
# L'élément à l'indice 0 est initialisé à 1, ce qui signifie qu'il n'y a qu'une façon de représenter 0 (en utilisant aucune somme).
# Les autres éléments (indices 1 à 300) sont initialisés à 0, car au début il n'y a aucune façon de représenter ces valeurs.
dp = [1] + [0] * 300

# Boucle sur les entiers de 1 à 17 inclus (range(1,18) donne 1,2,...,17).
for c in range(1, 18):
    # Calcul du carré de c pour l'utiliser dans l'algorithme.
    # Parcours tous les indices de 0 à (301 - c**2) (i.e., de 0 à 300 - c^2 inclus).
    for i in range(301 - c ** 2):
        # Pour chaque indice, on ajoute à dp[i + c^2] la valeur de dp[i].
        # Cela correspond à compter toutes les façons d'écrire 'i + c^2' 
        # en ajoutant 'c^2' à une manière de faire i.
        # Exemple : si dp[5] = 3 et c^2 = 4, alors il y a 3 façons d'obtenir 9 en ajoutant 4 à chaque combinaison qui donne 5.
        dp[i + c ** 2] += dp[i]

# Création d'une boucle infinie pour traiter les entrées de l'utilisateur.
while 1:
    # Demande à l'utilisateur d'entrer une valeur.
    n = input()
    # Vérifie si la valeur entrée est 0. Si c'est le cas, termine la boucle avec 'break'.
    if n == 0: break
    # Affiche le nombre de façons de représenter n comme une somme de carrés perfects.
    # Remarque : dans Python 2, 'input()' exécute eval(), ce qui donne un entier si on entre un nombre.
    print dp[n]