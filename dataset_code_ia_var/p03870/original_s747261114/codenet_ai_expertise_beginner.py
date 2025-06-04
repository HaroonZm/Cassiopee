import sys

def read_int():
    return int(sys.stdin.readline())

def main():
    n = read_int()
    a = []
    for _ in range(n):
        a.append(read_int())
    a.sort()
    x = 0
    for c in a:
        x ^= c
    s = set()
    for c in a:
        s.add(c ^ (c - 1))
    r = 0
    s = list(s)
    s.sort(reverse=True)
    for c in s:
        if x > 0 and len(bin(c)) == len(bin(x)):
            x ^= c
            r += 1
    if x != 0:
        print(-1)
    else:
        print(r)

main()