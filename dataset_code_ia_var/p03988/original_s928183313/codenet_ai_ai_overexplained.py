# Demander à l'utilisateur de saisir une valeur entière représentant le nombre d'éléments du tableau
n = int(input())

# Demander à l'utilisateur de saisir une ligne d'entiers séparés par des espaces, puis la convertir en liste d'entiers
a = list(map(int, input().split()))

# Créer un dictionnaire (structure clé-valeur) pour compter le nombre de fois où chaque entier apparaît dans la liste 'a'
cnt = {}  # Un dictionnaire vide pour stocker les fréquences

# Parcourir chaque indice de 0 à n-1 (tous les indices de la liste 'a')
for i in range(n):
    # Vérifier si la valeur 'a[i]' (l'élément en position i dans la liste) n'est pas déjà dans le dictionnaire de comptage 'cnt'
    if a[i] not in cnt:
        # Si la valeur n'est pas encore enregistrée dans le dictionnaire, l'ajouter avec un compteur initial de 1
        cnt[a[i]] = 1
    else:
        # Si la valeur est déjà présente dans le dictionnaire, incrémenter son compteur de 1 pour refléter une nouvelle occurrence
        cnt[a[i]] += 1

# Trouver la valeur maximale parmi tous les éléments de la liste 'a' grâce à la fonction 'max'
max_a = max(a)

# Initialiser une variable 'min_' avec une très grande valeur (arbitraire ici : 10^10) pour qu'elle soit remplacée rapidement par une valeur inférieure
min_ = 10000000000

# Calculer une valeur appelée 'diameter' comme étant la valeur maximale trouvée plus 1
diameter = max_a + 1

# Parcourir une boucle pour tous les entiers de 0 à (diameter-1), soit un total de 'diameter' tours
for i in range(diameter):
    # Calculer temporairement la valeur 'tmp' comme étant le plus grand entre 'max_a - i' et 'i'
    tmp = max(max_a - i, i)
    # Mettre à jour 'min_' pour garder la valeur la plus petite entre elle-même et 'tmp'
    min_ = min(min_, tmp)
    # Vérifier si la valeur 'tmp' existe dans le dictionnaire de comptage 'cnt'
    if tmp not in cnt:
        # Si 'tmp' n'existe pas dans le dictionnaire, afficher "Impossible" et arrêter brutalement le programme
        print("Impossible")
        exit()
    # Vérifier si le compteur associé à la valeur 'tmp' est égal à 0 (c'est-à-dire plus d'occurrences disponibles)
    if cnt[tmp] == 0:
        # Si aucune occurrence de 'tmp' restante, afficher "Impossible" et arrêter immédiatement le programme
        print("Impossible")
        exit()
    # Décrémenter le compteur de la valeur 'tmp' de 1 car elle vient d'être "utilisée"
    cnt[tmp] -= 1

# Parcourir toutes les clés restantes dans le dictionnaire 'cnt' (celles qui restent après la boucle précédente)
for i in cnt:
    # Vérifier si la clé 'i' a encore un compteur strictement supérieur à 0, c'est-à-dire si les occurrences n'ont pas toutes été utilisées
    # On vérifie en plus que 'i' est inférieure ou égale à 'min_', ce qui pourrait être interdit selon la logique du problème
    if cnt[i] > 0 and i <= min_:
        # Si une telle valeur existe, afficher "Impossible" et arrêter immédiatement l'exécution
        print("Impossible")
        exit()

# Si toutes les vérifications précédentes sont passées sans problème, afficher "Possible" car les conditions sont satisfaites
print("Possible")