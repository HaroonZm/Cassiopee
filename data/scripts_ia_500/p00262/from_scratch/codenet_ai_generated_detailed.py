def is_triangle_number(x):
    # Vérifie si x est un nombre triangulaire
    # k(k+1)/2 = x => résoudre k en fonction de x
    import math
    k = int((math.sqrt(8*x + 1) - 1) / 2)
    return k if k * (k + 1) // 2 == x else 0

def is_target_pattern(height_list):
    # Vérifie si la liste des hauteurs correspond à la forme triangulaire attendue
    # La hauteur doit commencer à 1 à gauche et augmenter de 1 vers la droite
    for i, h in enumerate(height_list, start=1):
        if h != i:
            return False
    return True

def perform_operation(heights):
    # Effectue une opération de réarrangement selon l'énoncé:
    # 1. Décale le bloc du bas vers la droite en plaçant tous les blocs du premier niveau à l'extrémité droite
    # 2. Fait tomber les autres blocs d'un niveau
    # 3. Comprime les blocs à gauche (pas d'espaces "vides")
    
    # the heights correspond to columns, each number is the height of the column.
    # on extrait la première "ligne" du bas (blocs blancs)
    bottom_row = 0
    for h in heights:
        if h > 0:
            bottom_row += 1
    
    if bottom_row == 0:
        return heights  # Pas de bloc tout en bas

    # Le nombre de colonnes initial
    n = len(heights)

    # Nombre total de blocs
    total_blocks = sum(heights)

    # On soustrait 1 à chaque colonne qui comporte au moins un bloc (laisser tomber les blocs)
    lowered = []
    for h in heights:
        if h > 0:
            lowered.append(h-1)
        else:
            lowered.append(h)

    # On construira une nouvelle liste de hauteurs
    # Les blocs extraits (les bottom_row blocs tout en bas) sont placés à l'extrémité droite, donc on ajoute une colonne à droite
    # Hauteur dans la nouvelle colonne = nombre de blocs extraits
    right_column_height = bottom_row

    # On enlève les colonnes avec hauteur 0 au milieu pour "comprimer"
    compressed = [h for h in lowered if h > 0]

    # Append la nouvelle colonne complètement à droite
    compressed.append(right_column_height)

    return compressed

def main():
    import sys

    while True:
        line = sys.stdin.readline()
        if not line:
            break  # EOF
        N_line = line.strip()
        if N_line == '0':
            break
        N = int(N_line)
        heights_line = sys.stdin.readline().strip()
        heights = list(map(int, heights_line.split()))
        
        total_blocks = sum(heights)
        k = is_triangle_number(total_blocks)
        if k == 0:
            # Impossible d'avoir la forme triangulaire si le total n'est pas un nombre triangulaire
            print(-1)
            continue

        # On ne peut pas dépasser 10000 opérations
        max_operations = 10000

        # Si la configuration initiale est déjà la bonne
        if is_target_pattern(heights):
            print(0)
            continue

        # On répète la transformation jusqu'à atteindre la forme triangulaire ou dépasser la limite
        current = heights
        count = 0
        seen = set()
        # Transformer la liste en tuple car elle est mutable et on veut détecter les cycles
        seen.add(tuple(current))
        result = -1
        while count < max_operations:
            count += 1
            current = perform_operation(current)
            # on teste la forme cible
            if len(current) == k and is_target_pattern(current):
                result = count
                break
            # détection cycle (cas ou la transformation tourne en rond)
            cur_t = tuple(current)
            if cur_t in seen:
                # On ne trouvera jamais le triangle, car on est dans un cycle
                break
            seen.add(cur_t)

        print(result)

if __name__ == "__main__":
    main()