def main():
    """
    Fonction principale qui lit les entrées, calcule le nombre minimum de déplacements nécessaires
    pour réorganiser une séquence d'entiers sous une certaine contrainte, et affiche le résultat.
    
    L'algorithme utilise une programmation dynamique sur des sous-ensembles de bits
    pour minimiser le nombre de déplacements.
    
    Entrées attendues (via input standard) :
    - N M : entiers, taille de la séquence et un entier supplémentaire non utilisé dans le code
    - Ensuite N lignes avec un entier par ligne (valeurs entre 1 et 20 inclus)
    
    Sortie : un entier, le coût minimal calculé.
    """
    
    # Lecture des deux entiers N et M
    N, M = map(int, input().split())
    
    # Lecture des N entiers, puis on décrémente chacun de 1 pour avoir un index 0-based
    a = [int(input()) - 1 for _ in range(N)]
    
    # Initialisation d'une matrice 20xN pour les préfixes cumulés
    # sum[j][i] contiendra le nombre d'occurrences de l'élément j jusqu'à l'indice i dans la liste a
    sum = [[0] * N for _ in range(20)]
    
    # Compteur du nombre total d'occurrences de chaque élément (entre 0 et 19)
    cnt = [0] * 20
    
    # ans_bit est un masque binaire représentant l'ensemble des éléments présents (bits à 1)
    ans_bit = 0
    
    # Construction des données auxiliaires
    for i in range(N):
        # On ajoute le bit correspondant à l'élément a[i] dans ans_bit
        ans_bit |= (1 << a[i])
        
        # Incrémentation du compteur pour cet élément
        cnt[a[i]] += 1
        
        # Marquage de la présence de a[i] à la position i (pour le préfixe)
        sum[a[i]][i] += 1
        
        # Mise à jour des préfixes cumulés pour chaque élément j
        if i - 1 >= 0:
            for j in range(20):
                sum[j][i] += sum[j][i - 1]
    
    # dp est un tableau de programmation dynamique :
    # dp[bitmask] = coût minimal pour avoir réorganisé les éléments correspondant aux bits 'bitmask' à 1
    # Initialisé avec une grande valeur (10**9) pour signifier "non calculé / infini"
    dp = [10 ** 9] * (1 << 20)
    
    # Cas de base : aucun élément utilisé, coût 0
    dp[0] = 0
    
    # Exploration de tous les sous-ensembles de l'ensemble {0,...,19}
    for bit in range(1 << 20):
        # Si l'état n'a pas été atteint ou est infini, on passe
        if dp[bit] == 10 ** 9:
            continue
        
        # v = nombre d'éléments déjà employés dans 'bit'
        v = 0
        for used in range(20):
            if (bit >> used) & 1:
                v += cnt[used]
        
        # Tentative d'ajouter un nouvel élément 'use' au sous-ensemble 'bit'
        for use in range(20):
            # Si cet élément n'existe pas dans la séquence, on l'ignore
            if cnt[use] == 0:
                continue
            
            # Si l'élément est déjà dans 'bit', on ne le re-ajoute pas
            if (bit >> use) & 1:
                continue
            
            # w = nouveau nombre d'éléments après ajout de 'use'
            w = v + cnt[use]
            
            # Calcul du nombre d'éléments 'use' qui restent à leur position dans l'intervalle [v, w-1]
            not_move = sum[use][w - 1]
            if v - 1 >= 0:
                not_move -= sum[use][v - 1]
            
            # Le nombre d'éléments 'use' à déplacer est le total moins ceux déjà à bonne position
            move = cnt[use] - not_move
            
            # Mise à jour du coût minimal pour le nouvel état 'bit | (1 << use)'
            dp[bit | (1 << use)] = min(dp[bit | (1 << use)], dp[bit] + move)
    
    # Affichage du résultat final correspondant au sous-ensemble contenant tous les éléments présents
    print(dp[ans_bit])


if __name__ == "__main__":
    main()