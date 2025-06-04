# AOJ ITP2_5_A: Sorting Pairs - Style personnel atypique

duo = []
lignes = int(input())
while len(duo) < lignes:
    XY = input().split()
    duo += [tuple(map(int, XY))]
sorted_duo = sorted(duo, key=lambda zz: (zz[0], zz[1]))
[print(j, k) for (j, k) in sorted_duo]