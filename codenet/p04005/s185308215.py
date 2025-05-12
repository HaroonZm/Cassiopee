L = [int(i) for i in input().split()]

if any(l % 2 == 0 for l in L):
    print(0)
else:
    L.sort()
    print(L[0] * L[1])