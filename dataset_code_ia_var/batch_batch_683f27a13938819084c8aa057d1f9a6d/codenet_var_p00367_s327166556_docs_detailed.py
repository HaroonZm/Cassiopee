def parse_time_intervals(n, lines):
    """
    Convertit chaque ligne d'entrée en une liste d'entiers correspondant aux horaires de début et de fin
    pour les trois catégories (a, h, b).
    
    Args:
        n (int): Le nombre de lignes à lire.
        lines (List[str]): Les lignes d'entrée, chacune contenant 12 entiers.
    
    Returns:
        Tuple[List[int], List[int], List[int], List[int], List[int], List[int]]: 
            Les heures de début et de fin (en minutes) pour 'a', 'h' et 'b'.
    """
    # Chaque entrée possède 12 entiers : hh1 mm1 hh2 mm2 hh3 mm3 hh4 mm4 hh5 mm5 hh6 mm6
    # Ces paires représentent, pour chaque catégorie (a, h, b), le début et la fin.
    entries = [list(map(int, line.split())) for line in lines]
    a_start = [x[0] * 60 + x[1] for x in entries]  # Convertit hh:mm en minutes
    a_end   = [x[2] * 60 + x[3] for x in entries]
    h_start = [x[4] * 60 + x[5] for x in entries]
    h_end   = [x[6] * 60 + x[7] for x in entries]
    b_start = [x[8] * 60 + x[9] for x in entries]
    b_end   = [x[10] * 60 + x[11] for x in entries]
    return a_start, a_end, h_start, h_end, b_start, b_end

def make_sets(start, end, n):
    """
    Génère une liste d'ensembles représentant la composition des membres actifs à chaque modification d'état temporelle.
    
    Args:
        start (List[int]): Les minutes de début de disponibilité pour chaque membre.
        end (List[int]): Les minutes de fin de disponibilité pour chaque membre.
        n (int): Nombre total de membres.
    
    Returns:
        List[set]: Chaque set représente l'ensemble des membres actifs lors d'un changement d'état entre 0h et 24h.
    """
    sets = []            # Stocke les ensembles résultants à chaque changement
    member = []          # Liste des indices actuellement actifs
    for t in range(1440):  # Pour chaque minute possible dans la journée (0 à 1439)
        upd = False
        for j in range(n):
            if start[j] == t:   # Si le membre j commence à ce moment
                member.append(j)
                upd = True
            if end[j] == t - 1: # Si le membre j finit juste avant ce moment
                member.remove(j)
                upd = True
        if upd:
            sets.append(set(member))
    return sets

def main():
    """
    Lit les données d'entrée, traite les créneaux horaires, génère les ensembles de disponibilité, puis
    calcule et affiche la taille maximale de l'intersection des ensembles de tous les rôles à un instant donné.
    """
    n = int(input())  # Nombre de membres/sujets
    lines = [input() for _ in range(n)]  # Lecture des n lignes d'entrée
    # Analyse des horaires pour chaque catégorie
    a_start, a_end, h_start, h_end, b_start, b_end = parse_time_intervals(n, lines)
    
    # Génération des ensembles pour chaque type de créneau (a, h, b)
    a_sets = make_sets(a_start, a_end, n)
    h_sets = make_sets(h_start, h_end, n)
    b_sets = make_sets(b_start, b_end, n)
    
    # Recherche du maximum d'intersection entre les ensembles a, h et b
    ans = 0
    for s1 in a_sets:
        for s2 in h_sets:
            for s3 in b_sets:
                # Calcule l'intersection des trois ensembles et met à jour le max trouvé
                intersection_size = len(s1 & s2 & s3)
                ans = max(ans, intersection_size)
                
    print(ans)

# Lancement du programme principal
if __name__ == "__main__":
    main()