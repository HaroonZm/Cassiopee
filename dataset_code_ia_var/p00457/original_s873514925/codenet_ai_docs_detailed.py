def myinput(n):
    """
    Lit une séquence d'entiers de l'utilisateur et retourne deux listes :
    - C : la liste des valeurs distinctes consécutives (compactées),
    - L : la liste des longueurs correspondantes de chaque bloc de C.

    Par exemple, pour la séquence d'entrée [1,1,2,2,2,3], C = [1,2,3], L = [2,3,1].

    Args:
        n (int): Nombre d'éléments à lire.

    Returns:
        list: Une liste contenant deux listes, [C, L].
    """
    C = [int(input())]  # Lit le premier élément et l'ajoute à C
    L = [1]             # Initialise la longueur du premier bloc à 1

    # Pour les n-1 éléments restants
    for i in range(1, n):
        c = int(input())  # Lit un nouvel élément
        if C[-1] == c:
            # Si égal au précédent, augmente la longueur du bloc courant
            L[-1] += 1
        else:
            # Sinon, commence un nouveau bloc
            C.append(c)
            L.append(1)
    return [C, L]


def check(C, L, low, hih):
    """
    Vérifie et somme les longueurs des blocs pouvant être "supprimés" selon la règle :
    - Supprime un bloc de taille >=4 si isolé, ou des blocs contigus identiques de taille >=4
      en élargissant vers la gauche et la droite.

    Args:
        C (list): Liste compacte des valeurs consécutives.
        L (list): Liste des longueurs pour chaque valeur dans C.
        low (int): Indice gauche du bloc à vérifier.
        hih (int): Indice droit du bloc à vérifier (souvent low+1).

    Returns:
        int: Longueur totale supprimée selon la règle.
    """
    m = len(C)
    ret = 0

    # Cas suppression d'un seul bloc à gauche
    if 0 <= low and L[low] >= 4 and (hih >= m or C[low] != C[hih]):
        ret += L[low]
        low -= 1

    # Cas suppression d'un seul bloc à droite
    if hih < m and L[hih] >= 4 and (low < 0 or C[low] != C[hih]):
        ret += L[hih]
        hih += 1

    # Cas où on peut combiner plusieurs suppressions si les blocs sont identiques 
    while 0 <= low and hih < m and C[low] == C[hih] and L[low] + L[hih] >= 4:
        ret += L[low] + L[hih]
        low -= 1
        hih += 1

    return ret


def solve(C, L):
    """
    Essaie de supprimer un élément de chaque bloc (en le "déplaçant" à gauche/droite)
    et vérifie si cela provoque une réaction en chaîne où plusieurs blocs peuvent
    être supprimés. Cherche l'opération qui maximise le nombre de suppressions.

    Args:
        C (list): Liste compacte des valeurs consécutives.
        L (list): Liste des longueurs pour chaque valeur dans C.

    Returns:
        int: Le nombre maximal d'éléments pouvant être supprimés via une réaction en chaîne.
    """
    m = len(C)
    ret = 0

    # Pour chaque bloc de la séquence compressée
    for i in range(m):
        L[i] -= 1  # Tente d'enlever 1 élément du bloc actuel

        # Essai: ajouter le "déplacé" à droite
        if i + 1 < m:
            L[i + 1] += 1
            if L[i] > 0:
                # Cas général: le bloc i existe toujours, on vérifie la suppression autour de (i, i+1)
                ret = max(ret, check(C, L, i, i + 1))
            else:
                # Si le bloc i disparaît, il faut vérifier entre (i-1, i+1)
                ret = max(ret, check(C, L, i - 1, i + 1))
            L[i + 1] -= 1  # Nettoie la modification

        # Essai: ajouter le "déplacé" à gauche
        if i - 1 >= 0:
            L[i - 1] += 1
            if L[i] > 0:
                ret = max(ret, check(C, L, i - 1, i))
            else:
                ret = max(ret, check(C, L, i - 1, i + 1))
            L[i - 1] -= 1  # Nettoie la modification

        L[i] += 1  # Restaure la valeur de L[i]

    return ret


while True:
    # Lecture du nombre d'éléments à traiter pour ce test
    n = int(input())
    if n == 0:
        # Condition d'arrêt
        break
    # On lit et compacte la séquence
    C, L = myinput(n)
    # On affiche le minimum d'éléments restant après la réaction optimale
    print(n - solve(C, L))