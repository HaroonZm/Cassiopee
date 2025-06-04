# Programme pour sélectionner deux étudiants avec la plus petite différence de scores
# selon les exigences de Dr. Tsukuba

def main():
    import sys

    # Lecture des données depuis l'entrée standard
    # On lira des ensembles jusqu'à ce que n=0 soit rencontré
    for line in sys.stdin:
        n_line = line.strip()
        if n_line == '0':  # Fin des données
            break
        n = int(n_line)
        # Lire la ligne suivante contenant les scores
        scores_line = sys.stdin.readline().strip()
        # Convertir en liste d'entiers
        scores = list(map(int, scores_line.split()))
        
        # Tri des scores pour faciliter la recherche de la plus petite différence
        scores.sort()
        
        # Initialiser la différence minimale avec une valeur très grande
        min_diff = 10**9 + 1
        
        # Parcourir les paires consécutives pour trouver la plus petite différence
        for i in range(n - 1):
            diff = scores[i+1] - scores[i]
            if diff < min_diff:
                min_diff = diff
            # Optimisation : si diff == 0, on ne peut pas faire mieux, on sort
            if min_diff == 0:
                break
        
        # Affichage de la différence minimale pour ce dataset
        print(min_diff)

if __name__ == "__main__":
    main()