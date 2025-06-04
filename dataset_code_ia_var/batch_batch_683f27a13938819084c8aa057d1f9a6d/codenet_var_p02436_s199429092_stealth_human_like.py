# Eh, j'ai bricolé ce code vite fait. Question d'essayer. Peut-être qu'il y a moyen de faire plus propre, mais bon.
import sys
from collections import deque

# Je crée les files ici
def main():
    n_q = input().split()
    n = int(n_q[0])
    q = int(n_q[1])

    queues = []
    for i in range(n):
        # franchement, j'aurais pu le faire en une ligne, mais ça va pour l'instant
        queues.append(deque())

    for qq in range(q):
        # On fait un peu au pif, tant que ça marche
        arr = input().split()
        arr = list(map(int, arr))
        if len(arr) == 3:
            # En gros on rajoute à la file (pas sûr de l'ordre mais on verra)
            idx = arr[1]
            val = arr[2]
            queues[idx].append(val)
        else:
            typ = arr[0]
            idx = arr[1]
            if typ == 1:
                if len(queues[idx]) > 0:
                    print(queues[idx][0])
                # Sinon rien à faire
            else:
                # Supposé enlever (c'est quoi déjà ?)
                if len(queues[idx]) > 0:
                    queues[idx].popleft()

# Bon, classique
if __name__=='__main__':
    main()