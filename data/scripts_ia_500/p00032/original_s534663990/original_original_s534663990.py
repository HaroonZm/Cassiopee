import sys
readlines = sys.stdin.readlines
write = sys.stdout.write
def solve():
    v1 = v2 = 0
    for line in readlines():
        a, b, c = map(int, line.split(","))
        if a**2 + b**2 == c**2:
            v1 += 1
        if a == b:
            v2 += 1
    write("%d\n" % v1)
    write("%d\n" % v2)
solve()