"""
Ce programme gère une file d'attente pour une station-service doté de plusieurs files ("rane").
Les véhicules peuvent entrer dans la station et être affectés à la file la plus courte, ou bien quitter leur file respective.
"""

# Lecture des valeurs initiales : n (nombre de files) et m (nombre d'opérations)
n, m = (int(x) for x in input().split())

# Initialisation des files comme des listes vides (une liste de listes)
rane = [[] for i in range(n)]

def getRane():
    """
    Recherche la file la plus courte parmi 'rane' et renvoie son index.

    Si plusieurs files ont le même nombre minimum d'éléments,
    renvoie l'index de la première trouvée.
    Si une file est vide, son index est immédiatement renvoyé.

    Returns:
        int: l'index de la file la plus courte.
    """
    index = 0       # Index de la file la plus courte
    min = 9999      # Longueur minimale des files (initialisée à une valeur élevée)
    for i in range(0, n):
        # On trouve la file avec le moins d'éléments
        if min > len(rane[i]):
            min = len(rane[i])
            # On renvoie immédiatement si la file est vide
            if min == 0:
                return i
            index = i
    return index

# Exécution des m opérations
for i in range(m):
    # Lecture du type d'opération (c) et de l'argument (num)
    c, num = (int(x) for x in input().split())

    if c == 0:
        # 給油終了 ("Refueling done") : retirer le premier véhicule de la file 'num'
        num -= 1  # Adapter l'index car l'entrée utilisateur commence à 1
        print(rane[num][0])  # Affiche le numéro du véhicule devant dans la file
        rane[num].pop(0)     # Supprime ce véhicule de la file
    else:
        # スタンドに入る ("Enter station") : affecte un véhicule à la file la plus courte
        index = getRane()        # Trouve l'index de la file la plus courte
        rane[index].append(num)  # Ajoute le véhicule à cette file