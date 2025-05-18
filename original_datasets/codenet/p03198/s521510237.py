from sys import stdin
from itertools import repeat
def f(a):
    n = len(a)
    l = [0] * (n + 1)
    st = [(a[0], a[0], 1)]
    pu = st.append
    po = st.pop
    for i in xrange(1, n):
        ad = 0
        y = a[i]
        k = 1
        while st and y > st[-1][0]:
            x, z, q = po()
            c = 0
            while x < y:
                x *= 4
                c += 2
            ad += c * q
            k += q
            y = z << c
        pu((a[i], y, k))
        l[i+1] = l[i] + ad
    return l

def main():
    n = int(stdin.readline())
    a = map(int, stdin.readline().split(), repeat(10, n))
    l = f(a)
    r = f(a[::-1])[::-1]
    ans = 10 ** 12
    for i in xrange(n + 1):
        if ans > l[i] + i + r[i]:
            ans = l[i] + i + r[i]
    print ans
main()