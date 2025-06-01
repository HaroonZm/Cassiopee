e = list(map(int, input().split()))
print("yes" if any(e[i] == e[j] and e[k] == e[l] for (i, j, k, l) in [(0,1,2,3), (1,2,0,3), (0,2,1,3)]) else "no")