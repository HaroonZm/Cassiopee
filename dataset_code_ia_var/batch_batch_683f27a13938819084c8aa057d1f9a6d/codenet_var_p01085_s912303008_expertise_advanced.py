from itertools import islice

def main(m, nx, nn):
    b = list(map(int, islice(iter(input, ''), m)))
    diffs = ((b[i - 1] - b[i], i) for i in range(nn, nx + 1))
    ans = max(diffs, key=lambda x: x[0])[1]
    print(ans)

while True:
    try:
        m, nmin, nmax = map(int, input().split())
        if m == nmax == nmin == 0:
            break
        main(m, nmax, nmin)
    except EOFError:
        break