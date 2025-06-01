from collections import deque

def main():
    """
    Programme principal qui résout un problème de déplacement d'éléments entre trois piles.
    
    La fonction lit plusieurs cas de test depuis l'entrée standard, où chaque cas est défini par :
        - n : nombre d'éléments dans la pile initiale.
        - m : nombre maximal d'opérations autorisées.
        - Trois listes représentant les piles a, b et c.
        
    Le but est de déterminer le nombre minimal de mouvements nécessaires pour trier la pile 'a' ou pour transférer tous les éléments dans la pile 'c' dans l'ordre de 1 à n.
    Les mouvements respectent certaines contraintes basées sur les règles du problème (similaires à celles du jeu de tours de Hanoi).
    
    La recherche est effectuée par une exploration en largeur (BFS) avec évitement des mouvements consécutifs inverses pour optimiser la solution.
    
    Affiche le nombre minimal de mouvements nécessaires, ou -1 si la condition n'est pas remplie dans la limite m.
    """
    while True:
        # Lecture de n et m, nombre d'éléments et nombre maximal de mouvements
        n, m = [int(i) for i in input().split()]
        # Condition d'arrêt : deux zéros signifient la fin des cas de test
        if n == 0 and m == 0:
            return
        
        # Lecture des piles a, b, c, chacune précédée par le nombre d'éléments (ignoré avec _)
        _, *a = [int(i) for i in input().split()]
        _, *b = [int(i) for i in input().split()]
        _, *c = [int(i) for i in input().split()]
        
        # On insère un 0 fictif au début de chaque pile pour simplifier les comparaisons de sommet (evite pile vide)
        a.insert(0, 0)
        b.insert(0, 0)
        c.insert(0, 0)

        # Initialisation de la file deque utilisée pour la recherche en largeur (BFS)
        # Chaque état contient les trois piles, le nombre d'opérations déjà effectuées, et le type de dernier mouvement (éviter les allers-retours immédiats)
        q = deque()
        q.appendleft([a, b, c, 0, -1])
        
        # Liste cible représentant l'état trié attendu des piles (de 0 à n inclus)
        tmp = [i for i in range(0, n+1)]

        # Boucle principale de BFS
        while q:
            # Extraction d'un état depuis la fin de la file (pop) pour une exploration FIFO classique
            a, b, c, d, t = q.pop()
            # d est le compteur d'opérations effectuées
            """
            # Debug : affichage des piles et séparateur
            print(a)
            print(b)
            print(c)
            print('=======')
            """
            # Si on dépasse le nombre maximal d'opérations, on affiche -1 et on arrête la recherche pour ce cas
            if d > m:
                print(-1)
                break
            # Condition d'arrêt : si la pile a ou c est dans l'état trié attendu (1..n dans l'ordre)
            if a == tmp or c == tmp:
                print(d)
                break
            # Génération des mouvements possibles selon règles:
            # Vérification que le dernier mouvement ne soit pas le mouvement inverse immédiat
            # et que le sommet de la pile source soit plus grand que celui de la pile destination
            
            # Mouvement de la pile a vers la pile b
            if a[-1] > b[-1] and t != 1:
                # Nouvel état avec dernier élément de a transféré à b, increment du compteur, t=0 pour marquer ce mouvement
                q.appendleft([a[:-1], b+[a[-1]], c[:], d+1, 0])
            
            # Mouvement de la pile b vers la pile a
            if b[-1] > a[-1] and t != 0:
                q.appendleft([a+[b[-1]], b[:-1], c[:], d+1, 1])
            
            # Mouvement de la pile b vers la pile c
            if b[-1] > c[-1] and t != 3:
                q.appendleft([a[:], b[:-1], c+[b[-1]], d+1, 2])
            
            # Mouvement de la pile c vers la pile b
            if c[-1] > b[-1] and t != 2:
                q.appendleft([a[:], b+[c[-1]], c[:-1], d+1, 3])

if __name__ == '__main__':
    main()