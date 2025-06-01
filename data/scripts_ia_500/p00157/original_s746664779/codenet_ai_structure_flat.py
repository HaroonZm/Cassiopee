while True:
    n = int(input())
    if n == 0:
        break
    dolls = []
    for _ in range(n):
        h, r = map(int, input().split())
        dolls.append((h, r))
    m = int(input())
    for _ in range(m):
        h, r = map(int, input().split())
        dolls.append((h, r))
    dolls = sorted(dolls, key=lambda w: (w[0], -w[1]))
    r = [d[1] for d in dolls]
    table = [1] * len(r)
    i = 0
    while i < len(r):
        j = 0
        while j < i:
            if r[j] < r[i]:
                if table[j] + 1 > table[i]:
                    table[i] = table[j] + 1
            j += 1
        i += 1
    print(max(table))