import sys
import bisect

def main():
    input = sys.stdin.readline
    S = input().rstrip()
    m = int(input())
    
    # Dictionnaires pour stocker les positions d'apparition de chaque préfixe et suffixe dans S
    # prefix_positions[p]: liste triée des indices où le préfixe p commence dans S
    # suffix_positions[s]: liste triée des indices où le suffixe s se trouve dans S (indice du début du suffixe)
    prefix_positions = dict()
    suffix_positions = dict()
    
    # Pour optimiser, on va d'abord collecter tous les préfixes et suffixes uniques demandés lors des requêtes
    queries = []
    prefix_set = set()
    suffix_set = set()
    for _ in range(m):
        x, y = input().rstrip().split()
        queries.append((x,y))
        prefix_set.add(x)
        suffix_set.add(y)
    
    # Prétraitement : pour chaque préfixe demandé, on cherche toutes ses occurrences dans S
    # De même pour chaque suffixe demandé, on cherche toutes ses occurrences (index du début du suffixe)
    # Pour retrouver occurrences rapidement, on utilise la recherche naïve KMP pourrait être trop complexe et peu nécessaire ici,
    # On utilisera str.find en boucle pour chaque motif, mêmes motifs multiples mais rationnel avec limites
    # Comme la somme des longueurs est petite (~2e5), le total des recherches reste dans une limite acceptable.
    
    def find_all_occurrences(text, pattern):
        positions = []
        start = 0
        while True:
            idx = text.find(pattern, start)
            if idx == -1:
                break
            positions.append(idx)
            start = idx + 1
        return positions
    
    for p in prefix_set:
        prefix_positions[p] = find_all_occurrences(S, p)
    for s in suffix_set:
        suffix_positions[s] = find_all_occurrences(S, s)

    # Maintenant, pour chaque requête (x, y), on veut la plus grande longueur d'un substring de S qui commence par x et finit par y
    # Soit start un indice de début du préfixe x, et end un indice de début du suffixe y, le substring est S[start : end + len(y)]
    # Pour que substring soit valide, il faut end + len(y) - 1 >= start + len(x) -1 (i.e. substring de longueur au moins len(x), et la position finale >= position de début)
    # Le substring doit commencer à start, finir à end+len(y)-1, donc longueur = (end + len(y)) - start
    # On cherche parmi tous couples (start,end) avec start in prefix_positions[x], end in suffix_positions[y] tel que end+len(y) > start (substring valide)
    # La longueur max est max((end + len(y)) - start)

    # Pour optimiser : on tri les listes prefix_positions[x] et suffix_positions[y] (déjà triés car trouvés en ordre croissant)
    # Pour chaque start, on veut trouver le plus grand end >= start + len(x) - len(y) 
    # ou plutôt simplifier, on veut end >= start (pour que substring au moins se construit)
    # Mais pour éviter chevauchement incorrect, on doit avoir end + len(y) > start, toujours vérifier
    
    # Méthode :
    # Parcourir les positions de prefix x, pour chaque on cherche dans suffix y l'end possible permettant longueur max.
    # Le plus grand end donne max longueur, on peut juste pour tous ends > start- len(y) chercher len max.
    # Une méthode simple :
    # - Trier suffix_positions[y]
    # - Pour chaque start dans prefix_positions[x], on cherche par bisect la plus grande suffix end >= start - on parcourt suffix ends >= start
    # - On choisit le suffix end >= start qui donne la plus grande longueur
    # Cela peut être couteux si trop souvent faire une recherche dans suffix_positions[y] pour chaque start.
    # Donc on peut inverser la démarche.
    
    # Optimisation finale:
    # Puisque le nombre d'occurrences peut être grand, et nombre de requêtes très grand, on va pré-calculer pour chaque requête.
    # Une solution acceptable:
    #   Pour chaque requête:
    #     1) obtenir listes prefix_positions[x] (starts)
    #     2) suffix_positions[y] (ends)
    #     3) on parcourt ends dans l'ordre croissant on garde leur max end+len(y)
    #     4) pour chaque start, on cherche via bisect dans ends la position la plus grande end >= start (afin substring valide)
    #     5) calculer substring length = (end + len(y)) - start
    #
    # Mais faire cela pour chaque requête risque d’être lent.
    #
    # Autre approche :
    #   for each query:
    #     on utilise deux pointeurs :
    #     i sur prefix_positions[x], j sur suffix_positions[y]
    #     on avance j tant que suffix_positions[y][j] + len(y) <= prefix_positions[x][i] (invalide)
    #     pour chaque start valid, on prend le suffix_position largest suffix_positions[y][j]
    #
    # Mais suffix_positions is sorted ascending, prefix_positions is sorted ascending
    # Pour augmenter efficacité, on parcourt les deux listes:
    #   pour chaque pos in suffix_positions[y] on cherche pos dans prefix_positions[x]
    #   ou inverse.
    #
    # Finalement, c’est plus rapide de faire :
    # pour chaque suffix end in suffix_positions[y]:
    #   calculer suffix_end_pos = end + len(y)
    #   stocker suffix_end_pos dans une liste sorted suffix_ends_adjusted
    #
    # Pour chaque start in prefix_positions[x]:
    #   chercher via bisect_left la plus petite suffix_end_pos >= start
    #   (les suffix_end_pos = end + len(y))
    #   si pas trouvé : aucun substring valide
    #   si trouvé : longueur = suffix_end_pos - start
    #   garder le max length
    
    # Implementation de cette dernière approche, pour chaque requête on fait un bisect multiple.
    
    output = []
    for x,y in queries:
        starts = prefix_positions.get(x, [])
        ends = suffix_positions.get(y, [])
        if not starts or not ends:
            # Pas d'occurrence soit pour x soit pour y
            output.append('0')
            continue
        
        suffix_ends_adjusted = [pos + len(y) for pos in ends]
        res = 0
        for start in starts:
            # chercher via bisect la plus petite suffix_end >= start
            idx = bisect.bisect_left(suffix_ends_adjusted, start)
            if idx == len(suffix_ends_adjusted):
                # pas de suffix_end >= start
                continue
            length = suffix_ends_adjusted[idx] - start
            if length > res:
                res = length
        output.append(str(res if res >= max(len(x), len(y)) else 0))
    
    print('\n'.join(output))


if __name__ == '__main__':
    main()