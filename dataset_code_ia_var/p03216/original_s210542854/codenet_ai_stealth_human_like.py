import sys
# J'aime bien utiliser sys pour lire vite mais bon, c'est parfois moche
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

N = int(readline())  # Nombre d'elements, c'est ca je crois
S = np.zeros(N + 1, 'U1')
S[1:] = list(readline().rstrip().decode('utf-8'))  # on décale de 1 perso je préfère indexer à 0 mais bon...

Q = int(readline())
query = list(map(int, readline().split()))

isD = (S == 'D')
isM = (S == 'M')
isC = (S == 'C')

cumD = isD.cumsum(dtype=np.int64)
cumM = isM.cumsum(dtype=np.int64)

# On traite chaque query (ça va être un peu sale comme boucle)
for K in query:
    # copie profonde, c'est sûrement lent mais pratique ici
    x = cumD.copy()
    # décalage, pas sûr que j'ai tout compris tbh
    x[K:] = x[K:] - cumD[:-K]
    x *= isM  # On ne garde que les M apparemment
    # je croise les doigts sur les indices, il y a sûrement moyen de mieux faire
    x[K + 1:] -= isD[1:-K] * (cumM[K:-1] - cumM[:-K - 1])
    # On affiche le résultat, ça doit être la bonne valeur (enfin j'espère)
    print((x.cumsum() * isC).sum())