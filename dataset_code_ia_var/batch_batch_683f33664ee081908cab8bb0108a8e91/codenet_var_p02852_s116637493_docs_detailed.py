from collections import deque

def min_steps_to_goal(N, M, S):
    """
    Calcule le chemin minimal pour atteindre la position N avec des sauts d'au plus M, en évitant les obstacles ('1').
    
    Arguments :
        N (int) : Dernière position à atteindre (0-indexé).
        M (int) : Longueur maximale d'un saut.
        S (str) : Chaîne binaire inversée représentant la trajectoire, où '0' permet de marcher et '1' bloque.
    
    Retourne :
        list : Liste du nombre de pas à chaque saut, dans l'ordre du trajet optimal, ou [-1] s'il n'existe pas de trajectoire valide.
    """
    # Ajoute des '1' fictifs à la fin pour éviter les vérifications de dépassement d'indice lors du parcours
    S = S[::-1] + '1' * M

    # Cas d'arrêt rapide : si M est supérieur ou égal à N, il suffit d'un saut unique
    if M >= N:
        return [N]
    
    # Initialisation d'une deque pour stocker les tailles de pas dans l'ordre inverse
    q = deque([])
    i = 0  # Position actuelle sur la chaîne
    j = 0  # Dernier point d'arrêt
    while i < N:
        f = 0  # Indicateur de possibilité de trouver le prochain pas
        # Recherche du plus grand saut valide allant de la fin du dernier saut (j) vers i+M en arrière
        for k in range(i + M, j, -1):
            if S[k] == '0':  # On a trouvé une case accessible
                f = 1        # Signal que la suite est possible
                break
        # Mettre à jour le dernier point d'arrêt
        j = i + M
        # Ajouter le nombre de pas effectués à la liste
        q.appendleft(k - i)
        i = k  # Se positionner à la nouvelle place atteinte
        if f == 0:
            # Si aucun nouveau saut n'est possible, on retourne -1
            return [-1]
    # Conversion de la deque en liste normale, résultat final : les pas effectués dans l'ordre
    return list(q)

def main():
    """
    Fonction principale. Lit l'entrée standard, effectue le traitement et affiche le résultat.
    """
    # Lecture de l'entrée
    N, M = map(int, input().split())
    S = input()
    # Appel du calcul
    result = min_steps_to_goal(N, M, S)
    if result == [-1]:
        print(-1)
    else:
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()