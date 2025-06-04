from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))  # Bon, on fait simple

cnt = Counter(a)
freqs = list(cnt.items())
freqs.sort(key=lambda t: t[1], reverse=True)  # On trie pour avoir les + fréq d'abord

if n <= k:
    print(0)  # Franchement ça sert à rien d'aller plus loin
else:
    reste = n
    for j in range(0,k):
        if j < len(freqs):
            reste -= freqs[j][1]
        else:
            continue  # just in case mais normalement pas nécessaire
    print(reste)  # on affiche le résultat, voilà