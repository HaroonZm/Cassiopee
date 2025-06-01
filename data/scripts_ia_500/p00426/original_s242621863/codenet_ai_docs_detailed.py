from collections import deque

def main():
    """
    Fonction principale qui lit plusieurs cas de test depuis l'entrée standard.
    Pour chaque cas, elle résout un problème de déplacement d'éléments entre trois piles 
    en un nombre minimal d'étapes, avec des contraintes spécifiques sur les déplacements.
    Le programme continue tant que n et m ne sont pas tous les deux nuls.
    """
    while True:
        # Lecture des deux entiers n (nombre d'éléments) et m (nombre maximal d'opérations)
        n, m = [int(i) for i in input().split()]
        # Condition d'arrêt si les deux sont à zéro
        if n == 0 and m == 0:
            return
        
        # Lecture des 3 piles a, b et c.
        # Chaque ligne commence par un nombre indiquant la taille, suivi des éléments.
        # On ignore ce premier nombre (_) et on prend le reste dans a, b, c.
        _, *a = [int(i) for i in input().split()]
        _, *b = [int(i) for i in input().split()]
        _, *c = [int(i) for i in input().split()]
        
        # Insertion d'un zéro au début de chaque pile.
        # Cela sert probablement d'épaisseur de base pour simplifier les comparaisons.
        a.insert(0, 0)
        b.insert(0, 0)
        c.insert(0, 0)

        # Initialisation d'une file double (deque) pour un parcours en largeur (BFS).
        # Chaque élément de la file est une liste comprenant :
        # les 3 piles actuelles, le nombre d'étapes effectuées (d),
        # et la dernière opération effectuée (t) pour éviter les mouvements inverses immédiats.
        q = deque()
        q.appendleft([a, b, c, 0, -1])

        # Une liste représentant la pile target "0,1,2,...,n", c'est-à-dire la configuration finale attendue
        tmp = [i for i in range(0, n+1)]

        # Boucle principale du BFS
        while q:
            # Extraction de l'état courant pour traitement
            a, b, c, d, t = q.pop()

            # Si le nombre d'étapes dépasse m, on abandonne et on imprime -1 indiquant l'impossibilité
            if d > m:
                print(-1)
                break

            # Si la pile a ou la pile c correspond exactement à la configuration finale,
            # on imprime le nombre d'étapes et on arrête le traitement de ce cas.
            if a == tmp or c == tmp:
                print(d)
                break

            # Les mouvements possibles entre piles avec vérifications des règles :

            # Déplacer le dernier élément de a vers b si plus grand que le sommet de b,
            # et que ce mouvement n'est pas simplement l'inverse d'un précédent déplacement
            if a[-1] > b[-1] and t != 1 and t != 0:
                # On enlève le dernier élément de a et on l'ajoute à b
                q.appendleft([a[:-1], b+[a[-1]], c[:], d+1, 0])

            # Déplacer le dernier élément de b vers a selon les mêmes contraintes
            if b[-1] > a[-1] and t != 0 and t != 1:
                q.appendleft([a+[b[-1]], b[:-1], c[:], d+1, 1])

            # Déplacer le dernier élément de b vers c selon les mêmes contraintes
            if b[-1] > c[-1] and t != 3 and t != 2:
                q.appendleft([a[:], b[:-1], c+[b[-1]], d+1, 2])

            # Déplacer le dernier élément de c vers b selon les mêmes contraintes
            if c[-1] > b[-1] and t != 2 and t != 3:
                q.appendleft([a[:], b+[c[-1]], c[:-1], d+1, 3])

if __name__ == '__main__':
    main()