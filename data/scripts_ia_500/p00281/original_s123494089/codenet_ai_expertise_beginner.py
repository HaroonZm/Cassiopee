n, m = input().split()
n = int(n)
m = int(m)

works = []
for i in range(n + 1):
    works.append([])

while True:
    s, t, e = input().split()
    s = int(s)
    t = int(t)
    e = int(e)
    if s == 0:
        break
    works[s - 1].append((t - 1, e))

l = int(input())
for _ in range(l):
    blst_input = input().split()
    blst = []
    for item in blst_input:
        blst.append(int(item))

    for i in range(n):
        total = 0
        for pair in works[i]:
            t = pair[0]
            e = pair[1]
            total += blst[t] * e
        print(total, end=' ')
    print()