from collections import Counter

def min_compressed_length(s):
    # Compter le nombre de chaque caractère
    count = Counter(s)
    
    # Séparer les lettres et les chiffres et les trier
    letters = sorted([c for c in count if c.isalpha()])
    digits = sorted([c for c in count if c.isdigit()])
    
    # Fonction pour trouver les intervalles contigus dans une liste de caractères ordonnés
    # par rapport à leur code ASCII
    def find_intervals(chars):
        intervals = []
        if not chars:
            return intervals
        start = prev = chars[0]
        for c in chars[1:]:
            if ord(c) == ord(prev) + 1:
                prev = c
            else:
                intervals.append((start, prev))
                start = prev = c
        intervals.append((start, prev))
        return intervals
    
    # Calcul des intervalles continus pour lettres et chiffres
    letter_intervals = find_intervals(letters)
    digit_intervals = find_intervals(digits)
    
    # La compression remplace chaque intervalle par "x-y" (2 chars + le tiret = 3 chars)
    # mais si l'intervalle ne fait qu'une lettre/chiffre, on garde 1 caractère.
    # Donc, pour chaque intervalle, la longueur compressée est
    # 3 si long intervalle (diff > 0), sinon 1
    
    def compressed_length(intervals):
        length = 0
        for start, end in intervals:
            if start == end:
                length += 1
            else:
                length += 3
        return length
    
    # On doit aussi compter les caractères qui ne sont ni lettres ni chiffres présents dans s
    # Or le problème indique que s ne contient que lettres minuscules et chiffres, donc pas de caractère autre.
    # Par contre, il peut y avoir répétitions de caractères.
    
    # La compression opère sur des groupes consécutifs de caractères après réordonnancement
    # En réordonnant, on peut mettre ensemble un seul intervalle pour toutes les occurrences du même caractère.
    # Le problème ne précise pas qu'une même lettre répétée est compressée en nombre réduit (ex: "aaa" → "a" ou "a-a")
    # Il faut donc compter combien de fois chaque caractère apparaît.
    # Mais la compression ne réduit pas le nombre de répétitions d'un même caractère,
    # il ne change que la représentation des séquences consécutives d'éléments consécutifs dans l'alphabet/digits.
    
    # La meilleure approche est donc de :
    # - Regrouper toutes les occurrences d'un même caractère (il est permis de réordonner)
    # - Pour chaque intervalle, la longueur finale sera le nombre d'occurrences de tous caractères dans cet intervalle
    #   remplacé par le nombre d'intervalles * (3 ou 1)
    #   MAIS la compression ne précise pas que l'on supprime répétitions, donc ? 
    #   En exemple : "1122334455" devient "1-5" (exemple answer=6)
    #   Le nombre minimal est la somme des longueurs minimisées par regroupement par intervalle
    
    # Correction :
    # La compression ne réduit pas les occurrences multiples d'un même caractère en un seul, elles restent toutes.
    # Donc on doit compter :
    # Pour un intervalle [start, end]
    # la longueur initiale est la somme des occurrences de tous characters dans l'intervalle
    # la longueur compressée est 3 (start-end) si intervalle>1 caractère, sinon nombre d'occurrences si simple caractère.
    # Le but est de minimiser la longueur après compression.
    
    # On doit donc partitionner les caractères en intervalles continus,
    # et pour chaque intervalle, le cout est :
    #   - si intervalle > 1 : 3 (ex: "a-d")
    #   - si intervalle = 1 : nombre d'occurrences de ce caractère (ex: "z" multiple fois)
    # Et on doit répartir les caractères pour minimiser la somme totale.
    
    # Remarque : On peut choisir de partitionner la liste triée des lettres en sous intervalles pour minimiser la taille
    # de sortis compressée. Pareil pour les chiffres.
    
    # On doit donc faire du DP pour partitionner la liste de lettres et la liste de chiffres.
    
    # Fonction récursive pour calculer la longueur minimale de compression sur un sousensemble ordonné de caractères
    def dp_min_length(sorted_chars):
        n = len(sorted_chars)
        
        # mémoriser par indice l'optimum
        memo = {}
        
        # pré-calcul occurrences cumulées pour gagner du temps
        occ = [count[c] for c in sorted_chars]
        prefix_sum = [0]*(n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i]+occ[i]
        
        def cost(i,j):
            # i,j inclusifs indices de characters dans sorted_chars
            # vérifier si chars forment une plage continue
            if ord(sorted_chars[j]) - ord(sorted_chars[i]) != j - i:
                return float('inf')  # intervalle discontinu interdit
            length = j - i +1
            total_occurrences = prefix_sum[j+1] - prefix_sum[i]
            if length == 1:
                # pas possible de compresser, doit écrire tous les occurrences
                return total_occurrences
            else:
                # on compresse en x-y avec 3 caractères
                return 3
        
        def dfs(i):
            if i == n:
                return 0
            if i in memo:
                return memo[i]
            res = float('inf')
            for j in range(i,n):
                c = cost(i,j)
                if c == float('inf'):
                    break  # pas continuity, pas besoin d'essayer plus loin
                res = min(res, c + dfs(j+1))
            memo[i] = res
            return res
        
        return dfs(0)
    
    # Calcul minimal séparément pour les lettres et les chiffres
    min_letters = dp_min_length(letters) if letters else 0
    min_digits = dp_min_length(digits) if digits else 0
    
    # La chaine compressée finale est la concaténation des compressions lettres + compression chiffres,
    # le problème montre dans l'exemple qu'une réorganisation put toute la rendre contiguë.
    # Le nombre total minimal est alors somme des min des 2 groupes.
    
    return min_letters + min_digits

# Lecture de l'entrée
s = input().strip()

# Calcul et affichage du résultat
print(min_compressed_length(s))