from sys import stdin
from itertools import islice

q = int(stdin.readline())
S = set()

for _ in range(q):
    words = stdin.readline().split()
    code = words[0]
    if code == '0':  # insert
        x = int(words[1])
        S.add(x)
        print(len(S))
    elif code == '1':  # find
        x = int(words[1])
        print(int(x in S))
    elif code == '2':  # delete
        x = int(words[1])
        S.discard(x)
    else:  # dump
        L, R = map(int, words[1:])
        # Choix optimal basé sur la taille de l'intervalle vs la taille du set
        if len(S) > R - L + 1:
            print(*(i for i in range(L, R + 1) if i in S), sep='\n')
        else:
            print(*sorted(x for x in S if L <= x <= R), sep='\n')