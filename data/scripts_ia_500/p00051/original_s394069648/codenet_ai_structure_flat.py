import sys
readline = sys.stdin.readline
write = sys.stdout.write
T = int(readline())
for _ in range(T):
    N = readline().strip()
    res = int("".join(sorted(N, reverse=1))) - int("".join(sorted(N)))
    write(str(res) + "\n")