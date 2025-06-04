from heapq import heappush, heappop

def process_test_case(n, intervals):
    """
    Calcule la somme maximale pour un cas de test donné.
    
    Chaque 'intervalle' est un triplet (k, l, r). On traite séparément les cas où l > r et l <= r.
    Les algorithmes utilisent un tas pour affecter des valeurs optimales à chaque groupe.
    
    Args:
        n (int): Nombre d'intervalles dans ce cas de test.
        intervals (list of tuples): Liste des triplets (k, l, r).
    
    Returns:
        int: La somme calculée pour ce cas de test.
    """
    group_x = []  # Intervalles où l > r
    group_y = []  # Intervalles où l <= r
    total_sum = 0

    # Séparer les intervalles selon la condition l > r
    for k, l, r in intervals:
        if l > r:
            # On utilise k, l, r tel que, plus tard, on triera sur k
            group_x.append((k, l, r))
        else:
            # Transformation pour gérer le groupe opposé de façon similaire
            group_y.append((n - k, r, l))
    
    # La fonction interne gère la logique de gestion de chaque groupe
    def handle_group(group):
        """
        Trie le groupe par k croissant, puis attribue de façon optimisée les valeurs.
        Utilise un tas pour extraire à chaque étape la meilleure valeur l ou r possible.
        
        Args:
            group (list of tuples): liste des intervalles du groupe
        
        Returns:
            int: somme des valeurs optimisées pour ce groupe
        """
        group.sort()  # Trie les intervalles par le 1er élément (k ou n-k)
        heap = []     # Tas min pour gérer les choix d'affectation
        local_sum = 0
        n_items = len(group)

        # On descend de n à 1 pour allouer les "slots"
        for position in range(n_items, 0, -1):
            # Ajoute dans le tas tous les intervalles dont k > position
            while group and group[-1][0] > position:
                _, l, r = group.pop()
                # On stocke (r-l, l, r) pour prioriser le gain le plus "rentable"
                heappush(heap, (r - l, l, r))
            # Si le tas est non vide, on choisit la valeur l la plus avantageuse
            if heap:
                _, l, _ = heappop(heap)
                local_sum += l
        # Ajouter la valeur r pour tous les éléments restants
        for _, _, r in group + heap:
            local_sum += r
        return local_sum

    # Calcul de la somme totale en traitant chaque groupe
    total_sum += handle_group(group_x)
    total_sum += handle_group(group_y)

    return total_sum

def main():
    """
    Fonction principale qui lit l'entrée, traite tous les cas de test et affiche les résultats.
    """
    i = input  # Lecture via input standard
    num_cases = int(i())
    for _ in range(num_cases):
        n = int(i())  # Nombre d'intervalles pour ce cas de test
        intervals = []
        for _ in range(n):
            # Lecture de chaque triplet (k, l, r)
            k, l, r = map(int, i().split())
            intervals.append((k, l, r))
        # Calcul et affichage du résultat pour ce cas
        print(process_test_case(n, intervals))

if __name__ == "__main__":
    main()