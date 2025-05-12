N = int(input())
S = [int(input()) for _ in range(N)]
table = [False] * (200 * 200 + 1)
table[0] = True
ma = 0
for s in S:
    ma += s
    for i in range(ma, -1, -1):
        table[i+s] |= table[i]
for i in range(ma, -1, -1):
    if i % 10 != 0 and table[i]:
        print(i)
        break
else:
    print(0)