import sys

def read_int_list():
    return list(map(int, sys.stdin.readline().split()))

def main():
    results = []
    while True:
        nmk = read_int_list()
        n = nmk[0]
        if n == 0:
            break
        m = nmk[1]
        k = nmk[2]
        size1 = n + 1
        size2 = n * m + 1
        r = []
        for i in range(size1):
            r.append([0.0] * size2)
        r[0][0] = 1.0
        for i in range(n):
            for j in range(i, n * m):
                if r[i][j] == 0:
                    break
                for kk in range(1, m + 1):
                    r[i + 1][j + kk] += r[i][j] / m
        t = 0.0
        for kk in range(n * m + 1):
            c = kk - k
            if c < 1:
                c = 1
            t += c * r[n][kk]
        results.append('{:0.9f}'.format(t))
    return '\n'.join(results)

print(main())