import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N = readline().strip()
    res = int("".join(sorted(N, reverse=True))) - int("".join(sorted(N)))
    write("%d\n" % res)
T = int(readline())
for i in range(T):
    solve()