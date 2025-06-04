def get_input():
    try:
        return input()
    except NameError:
        return raw_input()

while 1:
    line = get_input().split()
    n, m = int(line[0]), int(line[1])
    if not (n or m):
        break

    h = []
    i = 0
    while i < n:
        h.append(int(get_input()))
        i += 1

    w = [int(get_input()) for _ in range(m)]

    hs = dict()
    for x in range(len(h)):
        acc = h[x]
        hs.setdefault(acc, 0)
        hs[acc] += 1
        for y in range(x + 1, len(h)):
            acc += h[y]
            if acc in hs:
                hs[acc] = hs[acc] + 1
            else:
                hs[acc] = 1

    result, idx = 0, 0
    while idx < m:
        ws = w[idx]
        result += hs[ws] if ws in hs else 0
        k = idx + 1
        while k < m:
            ws += w[k]
            result += hs.get(ws, 0)
            k += 1
        idx += 1

    print(result)