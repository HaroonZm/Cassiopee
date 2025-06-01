from collections import deque

def main():
    """
    Programme principal qui lit des entrées successives définissant des configurations de plateformes
    et détermine pour chaque configuration si certaines conditions de déplacement sont satisfaites.

    Les entrées sont composées de plusieurs cas de test. Chaque cas de test commence par un entier M,
    suivi de N, le nombre de plateformes intermédiaires, puis N entiers représentant des offsets de déplacement.
    Le programme s'arrête lorsque M vaut 0.

    Pour chaque cas, le programme construit un graphe dirigé représentant les mouvements possibles entre plateformes,
    puis effectue deux parcours en largeur (BFS) pour vérifier si les ensembles de sommets atteignables depuis 
    la plateforme de départ et ceux pouvant atteindre la plateforme d'arrivée sont identiques.

    Affiche "OK" si les conditions sont vérifiées, sinon "NG".
    """
    while True:
        # Lecture de M, la portée maximale de saut
        M = int(input())
        if M == 0:
            # Condition d'arrêt du programme
            break
        
        # Lecture de N, le nombre de plateformes intermédiaires
        N = int(input())
        
        # Lecture des décalages D pour chaque plateforme intermédiaire
        # On ajoute 0 au début et à la fin pour représenter les plateformes de départ et d'arrivée
        D = [0] + [int(input()) for _ in range(N)] + [0]

        # Initialisation d'un graphe G représenté par une liste d'adjacence
        # Chaque sommet correspond à une plateforme (de 0 à N+1)
        G = [[] for _ in range(N + 2)]

        # u est un tableau indiquant si un sommet est accessible depuis la plateforme de départ
        u = [0] * (N + 2)
        
        # File pour le parcours en largeur (BFS) initialisé avec le sommet 0 (départ)
        que = deque([0])
        u[0] = 1  # Marquer la plateforme de départ comme visitée

        # Parcours en largeur pour explorer les déplacements possibles à partir du départ
        while que:
            v = que.popleft()
            # On regarde toutes les plateformes atteignables dans les M premiers indices après v
            for j in range(1, M + 1):
                # Calcul de la plateforme cible min(v+j, N+1) pour éviter de dépasser l'arrivée
                next_pos = min(v + j, N + 1)
                
                if D[next_pos] != 0:
                    # Si la plateforme cible a un décalage non nul, on applique ce décalage
                    to = max(min(next_pos + D[next_pos], N + 1), 0)
                else:
                    # Sinon, on reste sur la plateforme cible initiale
                    to = next_pos
                
                # Si la plateforme 'to' n'a pas encore été visitée, on l'ajoute à la file
                if not u[to]:
                    que.append(to)
                    u[to] = 1
                
                # On ajoute une arête inverse dans le graphe pour la traversée inverse ultérieure
                G[to].append(v)

        # z est un tableau indiquant si un sommet est atteignable depuis la plateforme d'arrivée
        z = [0] * (N + 2)
        
        # File pour un second parcours BFS, initialisé avec la plateforme d'arrivée (N+1)
        que = deque([N + 1])
        z[N + 1] = 1  # Marquer la plateforme d'arrivée comme atteinte

        # Parcours BFS à partir de l'arrivée en suivant les arêtes inverses pour déterminer
        # quels sommets peuvent atteindre l'arrivée
        while que:
            v = que.popleft()
            for w in G[v]:
                if z[w]:
                    # Si déjà visité, on continue
                    continue
                z[w] = 1
                que.append(w)

        # Vérification finale : les ensembles de sommets atteignables depuis le départ (u)
        # et ceux pouvant atteindre l'arrivée (z) doivent être égaux
        print("OK" if u == z else "NG")

if __name__ == "__main__":
    main()