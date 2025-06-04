import sys

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def main():
    results = []
    while True:
        wd = read_ints()
        w = wd[0]
        d = wd[1]
        if w == 0:
            break
        a = read_ints()
        b = read_ints()
        a.sort()
        b.sort()
        ai = 0
        bi = 0
        r = 0
        while ai < w or bi < d:
            if ai >= w:
                r += sum(b[bi:])
                break
            if bi >= d:
                r += sum(a[ai:])
                break
            if a[ai] == b[bi]:
                r += a[ai]
                ai += 1
                bi += 1
            elif a[ai] < b[bi]:
                r += a[ai]
                ai += 1
            else:
                r += b[bi]
                bi += 1
        results.append(r)
    print('\n'.join(str(x) for x in results))

main()