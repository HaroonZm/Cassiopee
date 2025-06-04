# Définir la valeur maximale de N, qui représente le nombre d'éléments pour lesquels nous allons pré-calculer les combinaisons de sommes de carrés parfaits.
N = 18  # Nous prenons ici les entiers de 0 à 17 inclus, nous aurons donc 18 valeurs au total.

# Construire une liste tbl qui contiendra les carrés parfaits correspondant à chaque entier de 0 à N-1.
# Utilisation d'une compréhension de liste pour élever chaque nombre au carré et placer le résultat dans la liste.
# Cela revient à: tbl[0] = 0*0, tbl[1] = 1*1, ..., tbl[17] = 17*17
tbl = [i**2 for i in range(0, N)]

# Créer un tableau 2D appelé dp (abréviation de "dynamic programming", programmation dynamique), 
# où dp[i][n] stockera le nombre de façons d'obtenir la somme n en utilisant uniquement les carrés parfaits de 0 à i inclus.
# La taille de la première dimension est N car nous avons N types de carrés parfaits.
# La taille de la deuxième dimension choisie arbitrairement ici comme 600, 
# car le problème considère que la somme maximale à traiter est inférieure à 600.
dp = [[0 for j in range(600)] for i in range(N)]

# Initialiser la cellule de base de notre tableau : 
# il y a exactement une seule manière d'obtenir la somme 0 avec aucun carré parfait (i=0 et n=0) : ne rien prendre du tout.
dp[0][0] = 1

# Remplir le tableau dp en utilisant la programmation dynamique.
# L'objectif est de compter, pour chaque i (type de carré parfait utilisé), 
# combien de façons différentes il existe pour obtenir chaque valeur n.
for i in range(1, N):  # Parcourir chaque type de carré parfait à partir de 1 (on a déjà traité 0)
    for n in range(300):  # Parcourir les sommes possibles, ici les valeurs de n de 0 à 299
        # Premièrement, reporter les façons d'obtenir la somme n sans utiliser le carré parfait de rang i.
        # Cela veut dire que toutes les combinaisons trouvées pour obtenir n avec les carrés précédents
        # restent valides même en ajoutant une nouvelle pièce (carré parfait).
        dp[i][n] += dp[i-1][n]
        # Deuxièmement, considérer combien de façons il existe d'obtenir la somme n+j
        # en ajoutant un ou plusieurs exemplaires du carré parfait courrant tbl[i] à la somme de base n.
        # Pour chaque multiple de tbl[i] (appelé ici j) ajouté à n, ajouter aux façons de faire n+j  
        # toutes celles qui permettent déjà de faire n avec les carrés précédents.
        for j in range(tbl[i], 300, tbl[i]):
            # Ici, pour chaque pas de j égal à tbl[i], on avance de tbl[i] à chaque itération, 
            # pour couvrir toutes les multiples utilisables à partir de n.
            # On ajoute alors au nombre de combinaisons de somme n+j toutes les façons déjà disponibles pour obtenir n.
            dp[i][n+j] += dp[i-1][n]

# Entrer en boucle infinie pour traiter les requêtes de l'utilisateur (jusqu'à ce qu'il saisisse 0 pour arrêter).
while True:
    # Lire un nombre entier depuis l'entrée standard (systèmatiquement une chaîne de caractères, il faut donc convertir en int).
    n = int(input())
    # Si n vaut 0, cela indique à notre programme qu'il doit arrêter de traiter les entrées, donc on rompt la boucle.
    if n == 0: break
    # Afficher le nombre de façons différentes d'obtenir la somme n avec tous les carrés parfaits disponibles.
    # Pour cela, on affiche la valeur contenue dans dp[N-1][n] qui a été pré-calculée.
    print(dp[N-1][n])