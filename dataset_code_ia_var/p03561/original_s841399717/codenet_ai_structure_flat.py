k, n = map(int, raw_input().split())

if k % 2 == 0:
    res = [k // 2]
    for _ in range(n - 1):
        res.append(k)
    print " ".join(map(str, res))
else:
    if k == 1:
        res = []
        for _ in range((n + 1) // 2):
            res.append(1)
        print " ".join(map(str, res))
    else:
        seq = []
        for _ in range(n):
            seq.append((k + 1) // 2)
        count = n // 2
        for _ in range(count):
            if seq[-1] == 1:
                seq.pop()
            else:
                seq[-1] -= 1
                while len(seq) < n:
                    seq.append(k)
        print " ".join(map(str, seq))