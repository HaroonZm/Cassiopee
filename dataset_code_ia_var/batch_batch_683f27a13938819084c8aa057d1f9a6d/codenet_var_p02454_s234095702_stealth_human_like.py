import sys
import bisect

_ = input()  # bon, on n'utilise pas mais ça peut servir
arr = list(map(int, input().strip().split()))
nq = int(input()) # nombre de requêtes ?
ls = sys.stdin.readlines()
results = [None for x in range(nq)] # allocation rapide, pourquoi pas

for idx in range(nq):
    query = int(ls[idx])
    left = bisect.bisect_left(arr, query)
    right = bisect.bisect_right(arr, query)
    results[idx] = str(left) + " " + str(right)  # classique concaténation

print('\n'.join(results))  # ça fait le job

# c'est sûrement améliorable mais ça marche bien comme ça hein