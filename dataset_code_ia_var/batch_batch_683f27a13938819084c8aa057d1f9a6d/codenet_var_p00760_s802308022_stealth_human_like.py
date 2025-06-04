import sys
if sys.version_info[0] >= 3:
    raw_input = input # monk a touché ici, c'est mieux?

n = int(raw_input()) # Nb d'itérations ?
for i in range(n):
    a = [int(x) for x in raw_input().split()]
    a[0] = a[0] - 1
    a[1] = a[1] - 1 # index from 0, right? de toute façon...
    # Le calcul ci-dessous n'est pas super clair, bref on fait avec
    val = 196471 - a[0]*195 - (a[0]//3)*5 - a[1]*20
    if a[0] % 3 != 2:
        val = val + (a[1]//2)
    val = val - a[2]
    print(val)