def solve():
    import sys
    sys.setrecursionlimit(10**7)
    
    # On va lire plusieurs datasets jusqu'à ce qu'on ait 0 0 en entrée.
    # Pour chaque dataset, on doit trouver un arbre de décision optimal pour identifier tout objet
    # en posant des questions (features) qui minimisent le pire cas du nombre de questions.
    #
    # Approche:
    # - Les objets sont représentés par des entiers (bitmask) selon leurs features.
    # - On veut construire un arbre binaire qui partitionne l'ensemble des objets jusqu'à
    #   un seul objet par feuille.
    # - Chaque noeud correspond à poser une question sur une feature non encore utilisée.
    # - On cherche à minimiser la profondeur maximale (hauteur) de l'arbre.
    #
    # On utilisera une DFS avec mémorisation:
    # - l'état est l'ensemble des objets restants à identifier et les features restants non utilisées.
    # - on teste chaque feature pour partitionner l'ensemble en objets "oui" (feature=1) et "non" (feature=0)
    # - on choisit la feature qui minimise le maximum entre les deux partitions (pire cas)
    #
    # Optimisations:
    # - Utiliser un encodage des objets restants sous forme d'un frozenset ou tuple d'indices
    #   - ou même mieux, une représentation en bitmask car n ≤ 128 -> on peut utiliser un tuple d'entiers
    # - Mémoriser les résultats dans un dict (memo)
    #
    # Limites:
    # - m ≤ 11, n ≤ 128, ce qui reste gérable avec un bon pruning.
    
    input = sys.stdin.readline
    
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break
        
        objs = []
        for _ in range(n):
            line = input().strip()
            # Convertir chaîne binaire en int
            obj = int(line, 2)
            objs.append(obj)
        
        # Memo dict:
        # clé: tuple(sorted objects indices), features_used_bitmask
        # value: minimal max depth to identify all objects
        # Comme on utilise int pour les objets et features,
        # on mémorisera sur un objet frozenset des objets (ou indices) + mask features non utilisées
        from functools import lru_cache
        
        # Créons un mapping des objets indices:
        # On notera les objets par leur index dans objs pour un accès plus simple.
        obj_indices = tuple(range(n))
        
        # mask_features représente les caractéristiques disponibles (non utilisées)
        # Par défaut, toutes les m caractéristiques peuvent etre utilisées: mask = (1 << m) -1
        FULL_MASK = (1 << m) - 1
        
        @lru_cache(None)
        def dfs(objects_tuple, available_features_mask):
            # objects_tuple: tuple des indices des objets encore à distinguer
            # available_features_mask: int binaire représentant les features pas encore posées
            
            length = len(objects_tuple)
            # Cas de base : si un seul objet, plus besoin de question
            if length == 1:
                return 0
            
            # Si plus aucune feature n'est disponible mais plusieurs objets restent => problème,
            # mais problème ne peut pas arriver car chaque objet est différent sur au moins une feature.
            if available_features_mask == 0:
                # Pas de questions possibles, mais plusieurs objets à distinguer => impossible
                # En théorie ne doit pas arriver car chaque objet diffère par une feature.
                # Pour être sûrs, on renvoie un grand nombre.
                return 10**9
            
            best = 10**9
            
            # On teste chaque feature disponible
            for f in range(m):
                if (available_features_mask & (1 << f)) == 0:
                    continue
                
                # Partitioner les objets selon valeur de cette feature
                group_yes = []
                group_no = []
                for idx in objects_tuple:
                    if (objs[idx] & (1 << (m - f - 1))) != 0:
                        group_yes.append(idx)
                    else:
                        group_no.append(idx)
                
                # Si une des deux partitions est vide, la question ne sert à rien pour cette étape
                if len(group_yes) == 0 or len(group_no) == 0:
                    continue
                
                # On retire cette feature du mask
                new_features_mask = available_features_mask & (~(1 << f))
                
                # Résoudre récursivement les deux sous-ensembles
                depth_yes = dfs(tuple(group_yes), new_features_mask)
                depth_no = dfs(tuple(group_no), new_features_mask)
                
                # La profondeur de ce noeud correspond au max du sous-arbre + 1 (la question posée ici)
                current_depth = 1 + max(depth_yes, depth_no)
                
                if current_depth < best:
                    best = current_depth
            
            # Si on n'a pas trouvé de feature qui divise, donc on ne peut pas distinguer,
            # Cela veut dire que les objets restants sont identiques sous features restantes (impossible selon l'énoncé).
            if best == 10**9:
                # pour éviter plantage, on renvoie une grande valeur
                return 10**9
            
            return best
        
        # Appel initial avec tous les objets et toutes les features dispo
        ans = dfs(obj_indices, FULL_MASK)
        print(ans)