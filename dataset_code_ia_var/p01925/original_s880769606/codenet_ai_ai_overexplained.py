def main():
    # La boucle principale du programme : elle s'exécute indéfiniment jusqu'à rencontrer une condition d'arrêt explicite à l'intérieur
    while (True):
        # Lecture d'une ligne d'entrée standard, séparation des éléments selon les espaces, conversion en entiers et assignation à N et M
        N, M = map(int, input().split())
        # Si on rencontre la ligne "0 0", on arrête l'exécution de la fonction et du programme
        if (N == 0 and M == 0):
            return
        # Initialisation d'une liste vide pour stocker les informations relatives à M sous-ensembles (groupes)
        skc = []
        # Pour chaque sous-ensemble (de 0 à M-1)
        for i in range(M):
            # Lecture de la ligne suivante, conversion de tous les éléments en entiers, et ajout du résultat à la liste skc
            skc.append(list(map(int, input().split())))
        # Création d'une liste point initialisée avec des zéros, de longueur N, pour stocker le total provisoire des points de chaque joueur
        # Par convention, chaque index dans 'point' représente le score du joueur numéro (index+1)
        point = [0 for i in range(N)]
        # Pour chaque sous-ensemble (chaque groupe de joueurs)
        for i in range(M):
            # Pour chaque joueur listé dans le groupe (le premier et le second élément ne sont pas des numéros de joueur)
            # On commence à l'indice 2 car les joueurs présents dans le groupe sont listés à partir de la 3ème position
            for j in range(2, len(skc[i])):
                # Incrémenter le score total du joueur correspondant par la valeur des points du groupe
                # skc[i][j] donne le numéro du joueur, mais il commence à 1 donc on décrémente de 1 pour obtenir l'index réel
                point[skc[i][j] - 1] += skc[i][0]
        # Création d'une liste point_fixed initialisée à 0, pour enregistrer des points fixes associés à certains joueurs concernés par une propriété spéciale du groupe
        point_fixed = [0 for i in range(N)]
        # Pour chaque groupe
        for i in range(M):
            # Si la propriété spéciale (ici, valeur du deuxième élément du groupe) est égale à 1
            if (skc[i][1] == 1):
                # Le joueur associé reçoit un ajout de points fixes (le montant du 1er élément du groupe)
                # L'indice du joueur particulier est donné par la troisième valeur dans la liste du groupe
                # On ajuste l'indice de 1 car les numéros de joueurs commencent à 1
                point_fixed[skc[i][2] - 1] += skc[i][0]
        # Initialisation de la variable maxPlayer qui contiendra le numéro du joueur ayant le maximum de points, initialement 0
        maxPlayer = 0
        # Initialisation de Max, qui stockera la valeur maximale des scores rencontrés, initialement 0
        Max = 0
        # Parcours de tous les scores pour trouver le joueur avec le score maximal
        for i in range(N):
            # Si le score du joueur courant dépasse Max
            if (Max < point[i]):
                # Mettre à jour Max avec la nouvelle valeur maximale
                Max = point[i]
                # Mettre à jour maxPlayer pour contenir le numéro du joueur gagnant (en ajoutant 1 parce que l'indexation commence à 0)
                maxPlayer = i + 1
        # Initialisation de la variable minPlayer pour retenir le numéro du joueur ayant le point fixe minimal (sous contrainte)
        minPlayer = 0
        # Initialisation de Min à une très grande valeur (ici 1e9) afin d'être sûr d'obtenir un minimum réel dans les scores
        Min = 1e9
        # Pour chaque joueur
        for i in range(N):
            # Si on tombe sur le joueur gagnant, on le saute (on veut un autre joueur pour minPlayer)
            if (i + 1 == maxPlayer):
                continue
            # Si le point fixe de ce joueur est inférieur à Min
            if (Min > point_fixed[i]):
                # On met à jour Min avec cette nouvelle valeur plus petite
                Min = point_fixed[i]
                # On stocke le numéro du joueur (toujours en prenant i+1 à cause de l'indexation 0)
                minPlayer = i + 1
        # Calcul et affichage du score final, basé sur la différence entre le score total du joueur maxPlayer
        # et le score fixe du joueur minPlayer, puis on ajoute 1 selon la logique de l'énoncé ou du problème
        # Remarquez que maxPlayer et minPlayer sont des numéros de joueur, donc on retranche 1 pour obtenir l'index de la liste
        print(point[maxPlayer - 1] - point_fixed[minPlayer - 1] + 1)

# Point d'entrée du programme, cette condition permet d'assurer que cette partie du code n'est exécutée que si ce fichier est exécuté directement, pas s'il est importé en tant que module
if __name__ == '__main__':
    main()