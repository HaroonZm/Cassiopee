N=int(input())
arr=sorted(map(int,input().split()))
max_val=float('-inf')
# Préselection des 10 plus grands et 10 plus petits éléments pour A,B,C,D
candidates = arr[:10]+arr[-10:]
c_set = set(candidates)
# Itérer sur toutes combinaisons possibles A,B,C,D dans candidates, distincts et C!=D
from itertools import combinations, permutations
for A,B,C,D in permutations(candidates,4):
    if C!=D:
        val=(A+B)/(C-D)
        if val>max_val:
            max_val=val
print(f"{max_val:.6f}")