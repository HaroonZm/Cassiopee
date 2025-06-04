n = int(raw_input())
Card = list()
for _ in xrange(n):
    Card.append([int(x) for x in raw_input().split()])
Cost = dict()
[Cost.update({(i, i): 0}) for i in xrange(n)]
for i in range(1, n):
    k = 0
    while k < n - i:
        b = k + i
        temp = []
        for m in xrange(k, k+i):
            temp += [Card[k][0]*Card[m][1]*Card[m+1][0]*Card[b][1] + Cost[(k, m)] + Cost[(m+1, b)]]
        Cost[(k, b)] = min(temp)
        k += 1
print Cost[(0, n-1)]