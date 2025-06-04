n = int(raw_input())
Card = [[] for _ in range(n)]
Cost = {}
for i in range(n):
    Card[i] = list(map(int, raw_input().split()))
    Cost[(i, i)] = 0
for i in range(1, n):
    for j in range(n - i):
        a = j + i
        Cost[(j, a)] = min([Card[j][0] * Card[k][1] * Card[k+1][0] * Card[a][1] + Cost[(j, k)] + Cost[(k+1, a)] for k in range(j, a)])
print Cost[(0, n-1)]