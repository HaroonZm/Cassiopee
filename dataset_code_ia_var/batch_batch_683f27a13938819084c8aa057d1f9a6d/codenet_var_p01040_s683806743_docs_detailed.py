def check_uruu(y):
    """
    Détermine si une année est bissextile.

    Args:
        y (int): L'année à vérifier.

    Returns:
        bool: True si l'année est bissextile, False sinon.
    """
    # Une année est bissextile si elle est divisible par 400,
    # ou si elle est divisible par 4 mais pas par 100.
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False

# Nombre de jours par mois pour une année non bissextile
nouruu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Nombre de jours par mois pour une année bissextile
uruu = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Lecture de 6 entiers correspondant à deux dates (année, mois, jour)
Y1, M1, D1, Y2, M2, D2 = map(int, input().split())

# Pré-allocation d'un tableau indiquant si le 13 de chaque mois est un vendredi
L = [0] * (2800 * 366)  # 2800 ans * 366 jours max par an

idx = 0  # Compteur global de jours depuis l'an 0
# On calcule d'abord combien de cycles de 2800 ans se trouvent avant l'année considérée pour Y1
di, Y1 = divmod(Y1, 2800)
ans1 = di * 4816  # Il y a 4816 vendredis 13 tous les 2800 ans
di, Y2 = divmod(Y2, 2800)
ans2 = di * 4816  # Même traitement pour Y2

# On parcourt les 2800 années du cycle
for y in range(0, 2800):
    # On choisit la table des jours selon que l'année est bissextile ou non
    if check_uruu(y):
        l = uruu
    else:
        l = nouruu
    # Pour chaque mois de l'année courante
    for m, n_days in enumerate(l, 1):
        # Calcule l'indice du 13ème jour de ce mois (décallage de 12 depuis le début du mois)
        d_13 = idx + 12
        # Si le 13 de ce mois est un vendredi (indice modulo 7 == 6 car 0=lundi, ..., 6=dimanche si le décalage initial est correct)
        if d_13 % 7 == 6:
            L[d_13] = 1  # Marque ce jour comme étant un vendredi 13

        # Calcule le nombre de vendredis 13 avant la date de départ (exclusive)
        if Y1 == y and M1 == m:
            # On additionne tous les vendredis 13 avant le jour D1-1 de Y1/M1
            ans1 += sum(L[:idx + (D1 - 1)])
        # Calcule le nombre de vendredis 13 avant ou le jour de la date d'arrivée (inclusive)
        if Y2 == y and M2 == m:
            # On additionne tous les vendredis 13 avant ou le jour D2 de Y2/M2
            ans2 += sum(L[:idx + D2])

        # Met à jour le compteur de jours pour passer au mois suivant
        idx += n_days

# Affiche la différence, c'est-à-dire le nombre de vendredis 13 dans l'intervalle demandé
print(ans2 - ans1)