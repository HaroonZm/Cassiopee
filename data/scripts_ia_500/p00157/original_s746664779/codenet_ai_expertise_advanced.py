from sys import stdin

def lis(seq):
    from bisect import bisect_left
    sub = []
    for x in seq:
        pos = bisect_left(sub, x)
        if pos == len(sub):
            sub.append(x)
        else:
            sub[pos] = x
    return len(sub)

for line in stdin:
    n = int(line)
    if n == 0:
        break
    dolls = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
    m = int(stdin.readline())
    dolls += [tuple(map(int, stdin.readline().split())) for _ in range(m)]

    dolls.sort(key=lambda w: (w[0], -w[1]))
    r = [h for _, h in dolls]
    print(lis(r))