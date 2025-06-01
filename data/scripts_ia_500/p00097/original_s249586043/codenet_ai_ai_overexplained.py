# Initialisation d'une liste bidimensionnelle `dp` de dimensions 10x1001.
# Cette liste est utilisée pour stocker des résultats intermédiaires.
# La structure `dp` est une "table" où chaque élément est initialisé à zéro.
# La première dimension représente un compteur (par exemple, le nombre d'éléments utilisés).
# La deuxième dimension représente une somme ou un état donné.
dp = [[0 for _ in range(1001)] for _ in range(10)]

# On initialise deux cases particulières :
# dp[1][0] = 1 signifie que pour 1 élément utilisé et somme 0, il y a une combinaison.
# dp[0][0] = 1 signifie que pour 0 élément utilisé et somme 0, il y a une "combinaison vide".
dp[1][0] = dp[0][0] = 1

# Boucle principale allant de 1 à 100 inclus.
# La variable `now` représente un nombre courant pris en compte dans la construction des combinaisons.
for now in range(1, 101):
    # Une boucle en ordre décroissant allant de 9 à 1 inclus.
    # `used` représente le nombre d'éléments utilisés dans la somme.
    for used in range(9, 0, -1):
        # Pour l'efficacité, on sauvegarde la référence à la sous-liste correspondant au nombre d'éléments utilisés.
        dpu = dp[used]
        # On récupère aussi la sous-liste pour un élément de moins utilisé (used-1).
        dpu_1 = dp[used - 1]
        # Parcours des sommes possibles allant de `now` jusqu'à 1000 inclus.
        for s in range(now, 1001):
            # On met à jour la valeur pour le nombre d'éléments `used` et somme `s` en ajoutant :
            # le nombre de façons d'obtenir la somme `s - now` avec `used - 1` éléments,
            # plus le nombre de façons d'obtenir la somme `s` avec `used` éléments déjà calculée.
            dpu[s] = dpu_1[s - now] + dpu[s]

# Une boucle infinie pour traiter des saisies multiples jusqu'à une condition d'arrêt.
while True:
    # Lecture de deux entiers séparés par un espace à partir de l'entrée standard.
    # map applique int à chaque élément du split pour obtenir des entiers.
    n, s = map(int, input().split())
    # Condition d'arrêt : si `n` est égal à zéro, on interrompt la boucle.
    if not n:
        break
    # Affiche le nombre de combinaisons pour `n` éléments utilisés et somme `s` en consultant `dp`.
    print(dp[n][s])