def main():
    """
    Point d'entrée du programme. Ce programme fusionne deux chaînes binaires pour générer la plus petite chaîne binaire possible qui contient les deux chaînes originales comme sous-séquences.
    """
    # Lecture des deux chaînes binaires d'entrée.
    p = input()
    q = input()
    
    # Longueur de chaque chaîne d'entrée
    lp = len(p)
    lq = len(q)
    
    # Préparation de tableaux pour accélérer la recherche du prochain "0" ou "1" dans chaque chaîne.
    # memop[i][0] : indice suivant où '0' apparaît à partir de p[i]
    # memop[i][1] : indice suivant où '1' apparaît à partir de p[i]
    memop = [[0, 0] for _ in range(lp + 2)]
    memoq = [[0, 0] for _ in range(lq + 2)]

    # Initialisation: placer des indices hors limites pour la facilité d'implémentation.
    memop[lp + 1] = [lp + 1, lp + 1]
    memoq[lq + 1] = [lq + 1, lq + 1]
    memop[lp] = [lp + 1, lp + 1]
    memoq[lq] = [lq + 1, lq + 1]
    
    # Remplissage inverse: pour chaque position, calculer les indices suivants pour '0' et '1'.
    for i in range(lp - 1, -1, -1):
        if p[i] == "0":
            memop[i][0] = i + 1          # Prochain '0' est à la position suivante
            memop[i][1] = memop[i + 1][1] # Prochain '1' inchangé du prochain indice
        else:
            memop[i][0] = memop[i + 1][0] # Prochain '0' inchangé
            memop[i][1] = i + 1           # Prochain '1' est à la position suivante
    
    for i in range(lq - 1, -1, -1):
        if q[i] == "0":
            memoq[i][0] = i + 1
            memoq[i][1] = memoq[i + 1][1]
        else:
            memoq[i][0] = memoq[i + 1][0]
            memoq[i][1] = i + 1
    
    # Initialisation de la table dp pour la programmation dynamique.
    # dp[i][j] = [min_steps_by_0, min_steps_by_1], représente le nombre minimal de caractères pour compléter la fusion depuis p[i] et q[j] selon le chiffre choisi ('0' ou '1').
    dp = [dict() for _ in range(lp + 2)]
    dp[lp + 1][lq + 1] = [0, 0]  # Base : fin des deux chaînes

    # Pile pour simuler la récursion et permettre la propagation des calculs
    q_stack = [[0, 0]]
    
    # Boucle principale pour remplir la table dp de façon itérative, en évitant la récursion.
    while q_stack:
        i, j = q_stack.pop()
        if j not in dp[i]:
            dp[i][j] = [None, None]
            a, b = None, None
        else:
            a, b = dp[i][j]
        if a is None or b is None:
            q_stack.append([i, j])  # Réexaminez ce point après calculs dépendants
            # Cas pour choisir '0' à la prochaine position
            if a is None:
                ap, bq = memop[i][0], memoq[j][0]  # Indices après ajout de '0'
                if bq not in dp[ap]:
                    dp[ap][bq] = [None, None]
                    q_stack.append([ap, bq])
                else:
                    aa, bb = dp[ap][bq]
                    if aa is None or bb is None:
                        q_stack.append([ap, bq])
                    else:
                        # On prend le minimum entre continuer avec '0' ou '1' et on ajoute '0' à la séquence
                        dp[i][j][0] = min(aa, bb) + 1
            # Cas pour choisir '1' à la prochaine position
            if b is None:
                ap, bq = memop[i][1], memoq[j][1]  # Indices après ajout de '1'
                if bq not in dp[ap]:
                    dp[ap][bq] = [None, None]
                    q_stack.append([ap, bq])
                else:
                    aa, bb = dp[ap][bq]
                    if aa is None or bb is None:
                        q_stack.append([ap, bq])
                    else:
                        dp[i][j][1] = min(aa, bb) + 1

    # Construction de la chaîne fusionnée en suivant la table dp
    q_stack = [[0, 0]]
    ans = ""
    while q_stack:
        i, j = q_stack.pop()
        a, b = dp[i][j]
        # Si l'on a atteint la fin de l'une des chaînes, on s'arrête
        if a == 0 or b == 0:
            break
        # On choisit le chiffre ('0' ou '1') correspondant au plus petit nombre d'étapes
        if a > b:
            q_stack.append([memop[i][1], memoq[j][1]])
            ans += "1"
        else:
            q_stack.append([memop[i][0], memoq[j][0]])
            ans += "0"
    print(ans)


if __name__ == '__main__':
    main()