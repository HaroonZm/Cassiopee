import sys

def read_input():
    """
    Lit les entrées à partir de stdin.

    Retourne :
        tuple : n (int) - nombre de joueurs,
                r (int) - nombre de lignes d'entrée (non utilisé ici),
                l (int) - heure de fin (ou limite supérieure de temps),
                lignes (list) - liste des lignes suivantes (chaque ligne est une chaîne de caractères).
    """
    f = sys.stdin
    n, r, l = map(int, f.readline().split())
    lines = f.readlines()  # Lire toutes les autres lignes d'entrée
    return n, r, l, lines

def main():
    """
    Lit les données du problème, traite les informations sur les joueurs et leurs scores,
    puis détermine le joueur avec la période de leader la plus longue.

    Affiche le numéro (1-indexé) du joueur ayant été leader le plus longtemps.
    """
    # Lire toutes les données nécessaires depuis stdin
    n, r, l, lines = read_input()
    
    # Initialiser deux listes :
    # - appearance : nombre de temps accumulé en tant que leader pour chaque joueur
    # - point : score courant (ou pointage) de chaque joueur
    appearance = [0] * n  # Temps passé comme leader pour chaque joueur
    point = [0] * n       # Score courant pour chaque joueur
    
    top = 0       # Index du joueur qui est actuellement en tête
    pre_t = 0     # Temps du dernier changement de leader ou de l'événement précédent

    # Traiter chaque événement ligne par ligne
    for line in lines:
        d, t, x = map(int, line.split())
        d -= 1  # Convertir d en base 0 (donné en base 1)
        
        # Ajouter le temps écoulé depuis le précédent événement au leader actuel
        appearance[top] += t - pre_t
        pre_t = t  # Mettre à jour le temps précédent
        
        # Mettre à jour le score du joueur concerné
        point[d] += x

        # Si un joueur obtient des points et n'est pas l'actuel leader
        if x > 0 and top != d:
            # Si le nouveau score est supérieur à celui du leader, il devient le leader
            if point[top] < point[d]:
                top = d
            # Si le score est égal, le joueur avec l'indice le plus petit prend la tête
            elif point[top] == point[d] and d < top:
                top = d
        # Si un joueur perd des points et qu'il est actuellement leader,
        # comparer tous les scores pour trouver le nouveau leader
        elif x < 0 and top == d:
            # Recherche du joueur avec le score maximal (plus petit indice en cas d'égalité)
            top = point.index(max(point))
    
    # Ajouter le temps restant jusqu'à l'heure de fin au leader final
    appearance[top] += l - pre_t

    # Recherche du joueur ayant passé le plus de temps comme leader (1-indexé)
    leader = 1 + appearance.index(max(appearance))
    print(leader)

if __name__ == '__main__':
    main()