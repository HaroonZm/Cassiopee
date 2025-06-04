import sys

def merge_delay_pattern(k, half1, half2):
    """
    Fusionne deux motifs de délais pour générer un motif de délai combiné.
    Chaque 'half' est une liste de tuples (position, délai).
    
    Args:
        k (int): La période totale du motif.
        half1 (list): Première moitié du motif sous forme [(position, délai), ...].
        half2 (list): Seconde moitié du motif sous forme [(position, délai), ...].
    
    Returns:
        list: Nouveau motif combiné sous forme de liste de tuples (position, délai).
    """

    len1 = len(half1)  # Taille du premier motif
    len2 = len(half2)  # Taille du second motif

    # Décompte et offset initiaux
    start, delay1_next = half1[0]  # Premier point du premier motif
    start2 = half2[0][0]           # Première position du second motif
    time1 = start - start2         # Décalage entre les deux motifs
    mid_start = start + time1 + delay1_next  # Point médian initial
    offset2_num_period = (mid_start - start2) // k  # Nombre de périodes complètes de k
    offset2_phase = mid_start - offset2_num_period * k  # Phase au sein de la période

    # Détermination du point de départ dans le deuxième motif
    for head2 in range(len2):
        if half2[head2][0] >= offset2_phase:
            head2 -= 1
            break
    head2 += offset2_num_period * len2
    head1 = 0  # Index dans le premier motif

    ret = []    # Liste de résultats
    prev = ()   # Variable pour éviter les doublons ou erreurs d'état
    half1.append((start + k, None))  # Sentinelle de fin pour boucler proprement

    pos1_next = start  # Variable de position suivante pour le motif 1
    pos2_next, delay2_next = half2[head2 % len2]  # Prochaine position & délai du motif 2
    pos2_next += (head2 // len2) * k              # Ajustement de la position si on répète
    mid = pos2_next                               # Point de synchronisation

    # Boucle principale pour intercaler les deux motifs
    while True:
        # Avancer dans le motif ayant la plus petite position suivante
        if mid <= pos2_next:
            if head1 == len1: break  # Fin du motif 1
            head1 += 1
            pos1, delay1 = pos1_next, delay1_next
            pos1_next, delay1_next = half1[head1]
        if pos2_next <= mid:
            head2 += 1
            pos2, delay2 = pos2_next, delay2_next
            pos2_next, delay2_next = half2[head2 % len2]
            pos2_next += (head2 // len2) * k

        # Calculs des motifs fusionnés selon cas particuliers des délais
        if delay1 == 0:
            mid = pos1_next + time1
            if delay2 == 0:
                if prev is not None:
                    ret.append((start, 0))
                    prev = None
            else:
                delay = pos2 + delay2 - time1 - start
                if prev != start + delay:
                    ret.append((start, delay))
                    prev = start + delay
            if pos2_next <= mid:
                start = pos2_next - time1
            else:
                start = pos1_next
        else:
            mid = pos1 + time1 + delay1
            if mid <= pos2_next:
                if delay2 == 0:
                    delay = delay1
                else:
                    delay = pos2 + delay2 - time1 - start
                if prev != start + delay:
                    ret.append((start, delay))
                    prev = start + delay
                start = pos1_next
    return ret

def get_delay_pattern(k, data, first, last):
    """
    Génère récursivement le motif de délais pour toutes les entrées fournies.
    Combine les motifs deux par deux jusqu'à ce que le motif final soit construit.

    Args:
        k (int): Période totale du motif.
        data (list): Liste de motifs individuels [[(pos, délai), ...], ...].
        first (int): Indice de début à traiter dans data.
        last (int): Indice de fin (non inclus) dans data.

    Returns:
        list: Motif de délai combiné correspondant à la plage data[first:last].
    """
    if last - first == 1:
        # Cas de base : un seul motif à ce niveau
        return data[first]
    middle = (first + last) // 2
    # Combinaison des deux moitiés par récursivité et fusion
    half1 = get_delay_pattern(k, data, first, middle)
    half2 = get_delay_pattern(k, data, middle, last)
    return merge_delay_pattern(k, half1, half2)

def solve():
    """
    Fonction principale de résolution.
    Lit les données depuis stdin, prépare les motifs, appelle la fusion
    et calcule le résultat attendu selon la logique métier.

    Returns:
        int: Le résultat du calcul demandé, ou -1 si impossible.
    """
    data = []  # Liste des motifs de délais individuels
    # Lecture de l'ensemble des entiers d'entrée
    int_list = [int(s) for s in sys.stdin.read().split()]

    n = int_list[0]  # Nombre de segments
    k = int_list[1]  # Longueur totale d'une période/cycle

    position = 0  # Accumulation de la position courante
    # Construction des motifs de retard/début selon les segments
    for i in range(2, (n + 1) * 2, 2):
        a = int_list[i]      # Longueur du segment courant
        b = int_list[i + 1]  # Marqueur spécial du segment (0 ou 1)
        if b == 1:
            a2 = a * 2
            if k < a2:
                # Condition impossible, motif non réalisable
                return -1
            # Construction du motif pour ce segment spécial
            data.append([(-position, 0), (-position + k - a2, a2)])
        position += a  # Mise à jour de la position pour le segment suivant

    # Si aucun segment spécial n'est traité, le résultat dépend uniquement du total des positions
    if not data:
        return position * 2

    # Génération du motif global fusionné
    delay_pattern = get_delay_pattern(k, data, 0, len(data))

    # Construction de la liste des (position, délai) adjacents pour évaluer les cas minimaux possibles
    pat_adj_pairs = zip(
        delay_pattern,
        delay_pattern[1:] + [(delay_pattern[0][0] + k, None)]
    )

    # Génération des décalages pertinents entre chaque paire successives de motifs pour le calcul du minimum
    delay_list = (
        pos + delay - next_pos
        for (pos, delay), (next_pos, _) in pat_adj_pairs
        if delay
    )

    # Retour du résultat final global (minimum trouvé + 2 * la longueur totale de segments)
    return position * 2 + min(delay_list, default=0)

print(solve())