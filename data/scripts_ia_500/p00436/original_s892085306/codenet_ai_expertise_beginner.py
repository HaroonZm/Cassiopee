n = int(input())
m = int(input())
ks = []
for i in range(m):
    ks.append(int(input()))

card = []
for v in range(1, n * 2 + 1):
    card.append(v)

for k in ks:
    if k == 0:
        c1 = card[:n]
        c2 = card[n:]
        tmp = []
        for i in range(n):
            tmp.append(c1[i])
            tmp.append(c2[i])
        card = tmp
    else:
        card = card[k:] + card[:k]

for v in card:
    print(v)