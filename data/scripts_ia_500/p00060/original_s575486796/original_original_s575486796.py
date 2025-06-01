import sys
readlines = sys.stdin.readlines
write = sys.stdout.write
def solve():
    for line in readlines():
        U = [0]*11
        a, b, c = map(int, line.split())
        U[a] = U[b] = U[c] = 1
        res = 0
        for x in range(1, 11):
            if U[x]:
                continue
            if a + b + x <= 20:
                res += 1
        if res*2 > 7:
            write("YES\n")
        else:
            write("NO\n")
solve()