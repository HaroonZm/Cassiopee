import sys

def LI():
    return list(map(int, sys.stdin.readline().split()))

def LS():
    return sys.stdin.readline().split()

def main():
    results = []
    while True:
        temp = LI()
        n = temp[0]
        if n == 0:
            break
        l = temp[1]
        a = []
        b = []
        for idx in range(n):
            s = LS()
            d = s[0]
            p = int(s[1])
            if p % 2 == 0:
                a.append((d, p, idx + 1))
            else:
                b.append((d, p, idx + 1))

        # Traitement des éléments avec p pair
        lc = 0
        rm = 0
        rf = False
        for tup in a:
            d = tup[0]
            p = tup[1]
            i = tup[2]
            if d == 'L':
                lc += 1
            m = p
            if d == 'R':
                m = l - m
            if rm < m or (rm == m and d == 'L'):
                rm = m
                if d == 'R':
                    rf = True
                else:
                    rf = False
        ri = lc
        if rf:
            ri += 1
        ari = -1
        if len(a) > 0 and ri - 1 < len(a):
            ari = a[ri - 1][2]

        # Traitement des éléments avec p impair
        lc = 0
        rf = False
        af = True
        for tup in b:
            d = tup[0]
            p = tup[1]
            i = tup[2]
            if d == 'L':
                lc += 1
            m = p
            if d == 'R':
                m = l - m
            if rm < m or (rm == m and d == 'L'):
                rm = m
                if d == 'R':
                    rf = True
                else:
                    rf = False
                af = False
        ri = lc
        if rf:
            ri += 1
        bri = -1
        if len(b) > 0 and ri - 1 < len(b):
            bri = b[ri - 1][2]

        if af:
            results.append(str(rm) + ' ' + str(ari))
        else:
            results.append(str(rm) + ' ' + str(bri))

    return '\n'.join(results)

print(main())