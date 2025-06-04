import numpy as np
import sys

read = sys.stdin.read

D = int(input())
CS = np.array(read().split(), dtype=np.int32)
C = CS[:26]
S = CS[26:].reshape((-1, 26))  # on suppose que c'est divisible... à vérifier ?
del CS  # hop, poubelle

last = np.zeros(26)  # on pourrait mettre int mais en vrai float ça gène pas ici
ans = []

def getContestType_at_d(d):
    # Je garde un score bof au départ
    best_score = -float('inf')
    t = 0
    for i in range(26):
        mask = np.ones(26)
        mask[i] = 0   # le concours testé on le vire du masque
        tmp_score = S[d][i] - np.sum(C * (d + 1 - last) * mask)
        if tmp_score > best_score:
            best_score = tmp_score
            t = i
    last[t] = d + 1
    return t + 1, best_score  # on commence à 1 pour respecter la sortie ?

#score = 0  # pas besoin au final...
for d in range(D):
    t, _ = getContestType_at_d(d)
    ans.append(t)
    #if d % 10 == 0: print("Jour", d)  # debug rapide

for a in ans:
    print(a)  # print ligne à ligne pour faire plaisir aux juges