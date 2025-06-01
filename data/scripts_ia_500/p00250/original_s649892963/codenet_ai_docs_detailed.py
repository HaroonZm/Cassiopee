def main():
    """
    Programme principal qui lit une série de cas tests depuis l'entrée standard.
    Chaque cas test commence par deux entiers N et M.
    Le programme s'arrête lorsque N et M sont tous deux égaux à zéro.
    
    Pour chaque cas test, le programme lit une liste de N entiers et calcule une certaine valeur maximale 
    liée aux sommes cumulées modulo M, en utilisant une structure de données Fenwick (arbre binaire indexé).
    Le résultat est ensuite affiché.
    """
    while True:
        # Lecture de deux entiers N et M depuis l'entrée
        N, M = map(int, input().split())
        
        # Condition d'arrêt : si N et M sont tous deux nuls, on termine le programme
        if N == M == 0:
            break
        
        # Initialisation de l'arbre Fenwick avec M+1 zéros.
        # data[k] représentera la fréquence cumulée pour les indices.
        data = [0] * (M + 1)

        def add(k, x):
            """
            Met à jour l'arbre Fenwick en ajoutant la valeur x à l'indice k.
            
            Args:
                k (int): L'indice à mettre à jour (1-based).
                x (int): La valeur à ajouter à data[k] et ses ancêtres.
            """
            while k <= M:
                data[k] += x
                # On passe à l'index suivant à mettre à jour en ajoutant le dernier bit significatif
                k += k & -k

        def get(k):
            """
            Calcule la somme cumulative des éléments d'indice 1 à k dans l'arbre Fenwick.
            
            Args:
                k (int): L'indice jusqu'auquel on veut la somme cumulative (1-based).
            
            Returns:
                int: La somme cumulée des valeurs de data de 1 à k.
            """
            s = 0
            while k > 0:
                s += data[k]
                # On descend à l'index père en enlevant le dernier bit significatif
                k -= k & -k
            return s

        # Calcul de la plus grande puissance de deux <= M, utilisée pour la recherche binaire dans lower_bound
        M0 = 2 ** (M - 1).bit_length()

        def lower_bound(x):
            """
            Recherche le plus petit indice i tel que la somme cumulative data[1..i] > x grâce à une recherche binaire.
            
            Args:
                x (int): La valeur seuil à dépasser.
            
            Returns:
                int: L'indice i + 1 où la somme cumulative dépasse x.
            """
            w = 0  # somme partielle courante
            i = 0  # indice courant
            k = M0  # pas de saut initial (puissance de 2 la plus grande <= M)
            
            while k > 0:
                # On vérifie si on peut sauter à i + k sans dépasser le seuil x
                if i + k <= M and w + data[i + k] <= x:
                    w += data[i + k]
                    i += k
                k >>= 1  # on divise k par 2 pour vérifier le prochain niveau
            return i + 1

        # Lecture de la liste des entiers K (taille N)
        K = list(map(int, input().split()))
        
        su = 0  # somme cumulative modulo M
        ans = 0  # résultat maximal à calculer
        
        # On initialise l'arbre Fenwick en ajoutant 1 à l'indice 1 (correspondant à somme 0)
        add(1, 1)
        
        # Pour chaque élément k de la liste
        for k in K:
            su = (su + k) % M  # mise à jour de la somme cumulée modulo M
            
            # Calcul du rang de su+1 dans l'arbre Fenwick
            v = get(su + 1)
            
            # Recherche par borne inférieure dans l'arbre Fenwick
            w = lower_bound(v) - 1
            
            # Si w vaut M, on le replace à 0 (car modulo M)
            if w == M:
                w = 0
            
            # Mise à jour de la réponse maximale
            ans = max(ans, (su - w) % M)
            
            # Ajout de la somme courante dans l'arbre Fenwick
            add(su + 1, 1)
        
        # Affichage du résultat pour ce cas test
        print(ans)

main()