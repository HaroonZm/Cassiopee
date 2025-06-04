# Demander à l'utilisateur de saisir deux entiers séparés par un espace :
# - 'n' : le nombre de requêtes ou d'éléments à traiter
# - 'd' : une contrainte supérieure sur 'cnt', à interpréter ultérieurement
n, d = map(int, input().split())

# Préparation d'une liste de sous-listes d'entiers:
# - Pour chaque 'i' de 0 à n-1 (soit 'n' fois), on lit une entrée utilisateur composée d'entiers séparés par des espaces
# - On convertit chaque valeur de la ligne du texte en entier grâce à map(int, ...)
# - On agrège ces entiers dans une liste avec list(map(...))
# - On rassemble toutes ces listes dans la grande liste 'lst'
# Enfin, on trie cette liste sur la première valeur de chaque sous-liste (par défaut du tri)
# Ajout à la liste d'un "élément sentinelle" : [10^20, 1], qui permet d'éviter un IndexError en accédant à lst[i + 1] lors de la dernière boucle
lst = sorted([list(map(int, input().split())) for _ in range(n)]) + [[10 ** 20, 1]]

# Initialisation de différents compteurs et états :
cnt = 0    # nombre d'opérations actuellement "en attente" ou "actives"
time = 0   # le temps courant, qui suit la simulation de l'avancement
floor = 1  # l'étage ou niveau en cours de traitement, initialisé à 1
ans = 0    # le coût cumulé ou résultat à afficher à la fin (somme pondérée selon cnt)

# Boucle pour traiter chaque événement/utilisateur/requête rangé dans 'lst'
# - On ne va que jusqu'à 'n' car l'entrée sentinelle n'est utilisée que pour le regard en avant
for i in range(n):

    # Extraire pour ce tour les valeurs 't' (temps de survenue/arrivée/disponibilité)
    # et 'f' (destination/étage voulu/autre signification selon le contexte)
    t, f = lst[i]

    # Vérifier si on ne peut pas satisfaire la requête courante :
    # - Si l'objectif de passer du niveau actuel 'floor' à la cible 'f' demande plus de déplacement que le temps imparti,
    #   c'est-à-dire s'il n'est pas possible d'arriver assez tôt
    # - Ou si le nombre d'opérations 'cnt' a atteint ou dépassé la limite 'd'
    if f - floor > t - time or cnt >= d:
        # Si c'est le cas, afficher -1 pour indiquer l'échec, puis arrêter la boucle immédiatement
        print(-1)
        break

    # Mise à jour du coût/résultat :
    # - Pendant la durée 't - time', il y a 'cnt' opérations actives
    # - Le coût total augmente de cnt * (t - time)
    ans += cnt * (t - time)

    # Une nouvelle opération s'ajoute à ce moment :
    cnt += 1

    # Le temps courant progresse jusqu'à l'instant 't', lié à cette requête
    time = t

    # Le niveau/étage courant devient celui visé ('f')
    floor = f

    # On prépare pour ce tour la lecture de la requête suivante (avec l'entrée sentinelle à la fin pour éviter l'erreur)
    next_t, next_f = lst[i + 1]

    # On vérifie si on peut ou doit effectuer un retour à l'état "initial" (par exemple revenir à l'étage 1) avant la prochaine requête :
    # - On calcule la somme : le temps courant + le temps pour descendre à l'étage 1 (floor - 1)
    #   puis le temps pour atteindre le prochain étage 'next_f' depuis l'étage 1 ((next_f - 1))
    # - Si ce total est inférieur ou égal au moment d'arrivée de la prochaine requête 'next_t'
    if time + (floor - 1) + (next_f - 1) <= next_t:
        # On profite donc de cet intervalle pour effectuer le retour à l'étage 1 :
        #   - chaque unité de temps (floor - 1) coûte 'cnt' en opérations/contributions
        ans += cnt * (floor - 1)
        # On remet à zéro le compteur d'opérations :
        cnt = 0
        # On avance le temps, puisqu'on vient de descendre à l'étage 1
        time += floor - 1
        # On se positionne à l'étage 1
        floor = 1

# La clause 'else' d'une boucle 'for' s'exécute uniquement si la boucle termine sans 'break'
else:
    # Afficher le résultat final, qui a été cumulé dans 'ans'
    print(ans)