def main():
    """
    Fonction principale pour lire les entrées, initialiser les variables et lancer la recherche dfs.
    Calcule une valeur minimale en fonction des contraintes données sur les partitions binaires.
    """
    # Lecture du nombre d'éléments depuis l'entrée standard
    N = int(input())
    # Lecture de la liste des contraintes pour chaque niveau
    A = [int(input()) for _ in range(N)]

    # Définition d'une constante pour l'infini (non utilisé ici mais courant dans les problèmes similaires)
    INF = 10**18
    # Le nombre total d'états possibles (2^N car chaque élément peut être "activé" ou non)
    N2 = 2**N

    def dfs(i, D):
        """
        Fonction de recherche approfondie (Depth-First Search) permettant d'explorer toutes les affectations possibles
        pour chaque niveau 'i', en respectant les contraintes définies dans la liste 'A'.

        Args:
            i (int): Le niveau courant à traiter (allant de 0 à N-1).
            D (List[int]): La configuration actuelle représentant le comptage des partitions binaires.

        Returns:
            int: La valeur minimale calculée suite à l'affectation du niveau 'i' et de ses suivants.
        """

        # Cas de base : si tous les niveaux ont été traités, retourne la somme actuelle
        if i == N:
            return sum(D)

        # Génère un masque binaire pour l'index courant 'i' (ex: pour i=1, b=2)
        b = 1 << i
        # Nombre d'affectations possibles à faire au niveau courant
        a = A[i]

        def sel(j, state, u):
            """
            Fonction récursive pour sélectionner les sous-ensembles de partitions valides sur ce niveau.

            Args:
                j (int): L'indice du sous-ensemble courant (dans [0, N2-1]).
                state (int): Encodage binaire représentant les sous-ensembles déjà utilisés à ce niveau.
                u (List[int]): Liste temporaire des indices sélectionnés pour cette itération.

            Returns:
                int: La valeur minimale obtenue après sélection et application de dfs pour les niveaux suivants.
            """

            # Si tous les sous-ensembles ont été considérés, applique la transition et lance l'étape suivante
            if j == N2:
                D2 = D[:]
                # Pour chaque partition sélectionnée, on "transfère" un élément vers le niveau courant
                for e in u:
                    D2[e] -= 1
                    D2[e | b] += 1
                # On attribue le reste des éléments au niveau courant (par défaut dans la partition seule)
                D2[b] = a - len(u)
                return dfs(i + 1, D2)

            # D'abord, essaye la solution sans sélectionner ce sous-ensemble :
            r = sel(j + 1, state, u)
            # Vérifie les contraintes pour sélectionner ce sous-ensemble :
            # 1. Il reste des éléments dans D[j]
            # 2. Les partitions sélectionnées ne se recouvrent pas (state & j == 0)
            # 3. On ne dépasse pas l'allocation possible (len(u) < a)
            if D[j] > 0 and (state & j) == 0 and len(u) < a:
                u.append(j)
                r = min(r, sel(j + 1, state | j, u))
                u.pop()
            return r

        # Lance la sélection pour tous les sous-ensembles au niveau courant
        return sel(0, 0, [])

    # Lance la procédure depuis le niveau 0, avec une configuration vide pour les partitions
    print(dfs(0, [0] * N2))


if __name__ == "__main__":
    main()