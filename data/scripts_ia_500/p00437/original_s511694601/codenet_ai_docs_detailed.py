def process_constraints():
    """
    Exécute un processus interactif de lecture et de traitement de contraintes basées sur des triplets d'indices et des résultats binaires.

    Pour chaque jeu de données fourni par l'utilisateur :
    - Lit un entier m, puis somme m entiers pour obtenir le nombre total d'éléments à traiter.
    - Si la somme est nulle, termine l'exécution.
    - Lit ensuite un entier n : le nombre de contraintes à traiter.
    - Initialise une liste 'fixed' de taille m avec des valeurs 2, représentant un état indéterminé pour chaque élément.
    - Lit n contraintes, chacune constituée de quatre entiers i, j, k, r.
        - Les indices i, j, k sont convertis en indices 0-based.
        - Si r == 1, met à jour l'état des éléments i, j, k à 1 dans 'fixed'.
        - Sinon, stocke la contrainte dans une liste 'failures' pour un traitement différé.
    - Après la lecture des contraintes, traite chaque contrainte de 'failures' selon la logique suivante :
        - Si l'un des éléments est fixé à 1, ajuste l'état des autres éléments associés à 0 en fonction des conditions données.
    - Affiche enfin la liste 'fixed' mise à jour, un élément par ligne.

    Le processus est répété jusqu'à ce que la somme m soit nulle.

    Exemple d'usage :
    > 3 0 1
    > 2
    > 1 2 3 1
    > 1 2 3 0
    ...
    """
    while True:
        # Lecture de m entiers puis calcul de leur somme
        m = sum(map(int, input().split()))
        if not m:
            # Si la somme est nulle, fin de la boucle et donc du programme
            break
        
        # Lecture du nombre de contraintes à traiter
        n = int(input())
        
        # Initialisation de la liste fixed à 2 pour tous les m éléments
        fixed = [2] * m
        
        # Liste pour stocker les contraintes "échecs" à traiter plus tard
        failures = []
        
        # Lecture des contraintes
        for _ in range(n):
            i, j, k, r = map(int, input().split())
            # Conversion des indices en base 0
            i, j, k = (x - 1 for x in (i, j, k))
            if r:
                # Si r == 1, on fixe les éléments correspondants à 1
                fixed[i] = fixed[j] = fixed[k] = 1
            else:
                # Sinon, on ajoute la contrainte à la liste des échecs
                failures.append((i, j, k))
        
        # Traitement différé des contraintes d'échec
        for i, j, k in failures:
            fi, fj, fk = (fixed[x] for x in (i, j, k))
            # Application de la logique conditionnelle pour ajuster fixed en fonction des contraintes
            if fi == 1:
                if fj == 1:
                    fixed[k] = 0
                elif fk == 1:
                    fixed[j] = 0
            elif fj == 1 and fk == 1:
                fixed[i] = 0
        
        # Affichage finale des états de fixed, un par ligne
        print('\n'.join(str(x) for x in fixed))


# Lancement du programme
process_constraints()