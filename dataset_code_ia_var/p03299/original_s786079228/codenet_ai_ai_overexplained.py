# Définition de la constante 'mod' qui servira à prendre tous les résultats du problème modulo (10^9 + 7).
# Cela permet d'éviter les débordements d'entier et de répondre aux contraintes classiques des problèmes de programmation.
mod = 10 ** 9 + 7

# Lecture d'un entier 'n' qui représente probablement le nombre d'éléments dans une séquence.
# La fonction input() lit une ligne du standard input sous forme de chaîne, puis int() convertit cette chaîne en entier.
n = int(input())

# Lecture d'une séquence de n entiers sur une seule ligne séparés par des espaces.
# input() lit la ligne, .split() découpe la chaîne selon les espaces, map(int, ...) convertit chacun des morceaux en entier.
# list() convertit enfin l'objet map en liste, assignée à 'H' qui contiendra les hauteurs ou valeurs analysées par le problème.
H = list(map(int, input().split()))

# Définition de la fonction 'solve' recevant une liste d'entiers 'h'.
def solve(h):
    # Si la liste des hauteurs est vide (cas de base, aucune hauteur à traiter) :
    if not h:
        return 1  # Il n'y a qu'une seule façon triviale de traiter une liste vide.

    # Si la liste ne contient qu'un seul élément :
    elif len(h) == 1:
        # Le résultat est 2 puissance la hauteur de cet unique élément, modulo mod.
        # pow(x, y, mod) calcule (x^y) % mod de façon efficace.
        return pow(2, h[0], mod)

    # Calcul de la taille effective (nombre d'éléments) de la liste 'h'.
    N = len(h)

    # Création d'une liste 'a' qui copie, via compréhension de liste, tous les éléments de 'h'.
    a = [h[i] for i in range(N)]

    # Conversion de la liste 'a' en ensemble (set) pour ne retenir que les valeurs uniques (élimination des doublons).
    a = list(set(a))

    # Tri de la liste 'a' afin de traiter les valeurs dans l'ordre croissant.
    a.sort()

    # Construction d'un dictionnaire de compression 'comp':
    # Chaque valeur unique trouvée dans 'a' se voit attribuer une position unique et croissante en partant de 1.
    comp = {i: e + 1 for e, i in enumerate(a)}

    # Construction d'un dictionnaire 'data' pour retrouver la valeur initiale à partir de la valeur compressée.
    # Parcourt toutes les clés de 'comp', et associe la clé comp[e] à la valeur originelle e.
    data = {comp[e]: e for e in comp.keys()}

    # Initialisation manuelle du dictionnaire 'data' pour deux clés : 
    # data[0] = 0 (initialisé puis écrasé par la ligne suivante), puis data[0] = 1.
    # ATTENTION : seule la dernière affectation est prise en compte et donc data[0] == 1 à la fin.
    # Cela semble être une astuce de code ou un héritage d'une version précédente.
    data[0] = 0
    data[0] = 1

    # AFFICHAGE COMMENTÉ = print(comp)
    # Il s'agit d'un débogage optionnel pour observer l'association valeur initiale <-> compacte.


    # Création et initialisation de la table de programmation dynamique 'dp'.
    # Il s'agit d'une liste à deux dimensions (matrice) de taille [N][len(a)+1], remplie de zéros.
    # Chaque dp[i][j] représente habituellement le nombre de façons d'atteindre une configuration donnée
    # à la position 'i' (indice de la hauteur h) et état compressé 'j' (hauteur compressée de l'étape).
    dp = [[0 for i in range(len(a) + 1)] for j in range(N)]

    # Traitement de la première transition de la séquence :
    # On commence avec l'indice i=0 qui correspond au premier élément de 'h',
    i = 0

    # Si la deuxième hauteur est supérieure ou égale à la première :
    if h[i + 1] >= h[i]:
        # On obtient les indices compressés id pour h[i] et id2 pour h[i+1].
        id = comp[h[i]]
        id2 = comp[h[i + 1]]

        # Pour toutes les valeurs entre id et id2 (compris) :
        # On considère qu'il existe 2 façons d'obtenir ces états à la prochaine étape.
        for j in range(id, id2 + 1):
            dp[i][j] = 2

        # Pour tous les indices inférieurs à id :
        # On ne peut obtenir cet état que d'une unique façon.
        for j in range(0, id):
            dp[i][j] = 1

    # Si au contraire la deuxième hauteur est inférieure à la première :
    else:
        # On obtient l'indice compressé correspondant à h[i+1].
        id = comp[h[i + 1]]

        # Pour tous les indices strictement inférieurs à id :
        # On élève 2 à la différence h[i] - h[i+1], modulo mod et on affecte la valeur dans la table dp.
        for j in range(0, id):
            dp[i][j] = pow(2, h[i] - h[i + 1], mod)

        # Calcul de la valeur dp[i][id] en multipliant 2 par (2^(différence) - 1), puis prise modulo mod.
        dp[i][id] = 2 * (pow(2, h[i] - h[i + 1], mod) - 1)
        dp[i][id] %= mod

        # On obtient l'indice compressé correspondant à h[i].
        id2 = comp[h[i]]

        # On ajoute 2 à la valeur dp[i][id], puis prise modulo mod.
        dp[i][id] += 2
        dp[i][id] %= mod

    # Boucle principale pour remplir la table dp pour les étapes suivantes :
    # On commence à la deuxième transition (i=1) et on termine à l'avant-dernière (N-2),
    # car la dernière hauteur h[N-1] sera traitée après.
    for i in range(1, N - 1):

        # Si la prochaine hauteur est au moins aussi grande que la courante :
        if h[i + 1] >= h[i]:
            id = comp[h[i]]
            id2 = comp[h[i + 1]]

            # Pour chaque j entre id et id2 :
            # Multiplie l'état dp précédemment atteint à h[i] par 2 pour chaque possibilité.
            for j in range(id, id2 + 1):
                dp[i][j] = (2 * dp[i - 1][id]) % mod

            # Pour les états en-deçà, on garde le même compte que précédemment.
            for j in range(0, id):
                dp[i][j] = dp[i - 1][j]

        # Si la prochaine hauteur est strictement plus basse :
        else:
            id = comp[h[i + 1]]
            id2 = comp[h[i]]

            # Pour chaque état inférieur à id :
            # On multiplie le nombre de façons de parvenir à chaque état plus bas par 2^(différence), modulo mod.
            for j in range(0, id):
                dp[i][j] = (pow(2, h[i] - h[i + 1], mod) * dp[i - 1][j]) % mod

            # Pour chaque état intermédiaire entre id (inclus) et id2 (exclu) :
            for j in range(id, id2):
                # Récupère la hauteur basse correspondante à l'index j, et la prochaine hauteur haute.
                low = data[j]
                up = data[j + 1] - 1

                # On additionne au nombre de manières d'atteindre l'état 'id', toutes les combinaisons issues de j.
                # La formule utilise les puissances pour compter les combinaisons, et soustrait les impossibles.
                dp[i][id] += dp[i - 1][j] * pow(2, h[i] - up, mod) * (pow(2, up - low + 1, mod) - 1)

            # Prise du modulo pour rester dans les limites.
            dp[i][id] %= mod

            # On ajoute 2 fois dp[i-1][id2] à dp[i][id], mod mod.
            dp[i][id] += 2 * dp[i - 1][id2]
            dp[i][id] %= mod

    # Calcul du résultat final 'ans'.
    ans = 0

    # Récupération de l'indice compressé de la dernière hauteur de la séquence.
    id = comp[h[-1]]

    # Pour chaque état antérieur à id :
    for i in range(0, id):
        # Récupération des bornes basse et haute correspondantes à la compression courante.
        low = data[i]
        up = data[i + 1] - 1

        # On ajoute au résultat toutes les combinaisons possibles à partir de ces états,
        # c'est-à-dire le nombre de façons d'être arrivé à ce stade multiplié par les options en hauteur finale.
        ans += dp[N - 2][i] * pow(2, h[-1] - up, mod) * (pow(2, up - low + 1, mod) - 1)
        ans %= mod

    # On ajoute 2 fois la valeur dp[N-2][id] pour les états correspondant à la plus grande hauteur.
    ans += 2 * dp[N - 2][id]
    ans %= mod

    # On retourne le résultat calculé pour la séquence h.
    return ans

# Calcul initial : pow(2, nombre de 1 dans la liste H, mod)
# Cela signifie que pour chaque 1 dans H, il y a deux possibilités (probablement à cause d'une séparation dans la logique du problème).
ans = pow(2, H.count(1), mod)

# On crée une liste 'check' contenant tous les indices i tels que H[i] == 1 :
# Cette liste repère tous les emplacements de 1 dans la séquence H.
check = [i for i in range(n) if H[i] == 1]

# On étend cette liste en rajoutant artificiellement aux extrémités -1 (avant le début) et n (après la fin) :
# Cela servira à gérer les intervalles de découpe de H sans cas particulier pour les bords.
check = [-1] + check + [n]

# On parcourt tous les intervalles entre des 1 dans la séquence :
for i in range(len(check) - 1):
    # Définition des bornes d'intervalle [l+1 : r], c'est-à-dire entre deux 1 consécutifs (ou au début/fin de la liste).
    l, r = check[i], check[i + 1]
    # On multiplie ans par le résultat de solve appliqué à la sous-séquence H[l+1:r].
    ans *= solve(H[l + 1:r])
    # On prend le résultat modulo 'mod'.
    ans %= mod

# Affichage du résultat final sur la sortie standard.
print(ans)