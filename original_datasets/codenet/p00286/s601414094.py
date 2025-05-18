from string import digits, ascii_uppercase

def parse(S, N, R):
    S = S + "$"
    cur = 0
    def expr():
        nonlocal cur
        *r0, = range(N)
        while 1:
            r = term()
            r0[:] = [r0[e] for e in r]
            if S[cur] != '+':
                break
            cur += 1 # '+'
        return r0
    def term():
        nonlocal cur
        if S[cur] in digits:
            # m(expr)
            k = number()
            if S[cur] == '(':
                cur += 1 # '('
                r = expr()
                cur += 1 # ')'
            else:
                r = identity()
            r = power(r, k)
        else:
            r = identity()
        return r
    def power(r, k):
        *r0, = range(N)
        r1 = r[:]
        while k:
            if k & 1:
                r0[:] = [r0[e] for e in r1]
            r1[:] = [r1[e] for e in r1]
            k >>= 1
        return r0
    def number():
        nonlocal cur
        v = 0
        while S[cur] in digits:
            v = 10*v + int(S[cur])
            cur += 1 # '0' ~ '9'
        return v
    def identity():
        nonlocal cur
        r = R[S[cur]]
        cur += 1 # 'A' ~ 'Z'
        return r
    return expr()

def main():
    N, K = map(int, input().split())
    R = {}
    for i in range(K):
        p, h = input().split(); h = int(h)
        *r, = range(N)
        for i in range(h-1):
            *g, = map(int, input().split())
            for j in range(N-1):
                if g[j]:
                    r[j], r[j+1] = r[j+1], r[j]
        R[p] = r
    E = int(input())
    for i in range(E):
        S = input()
        res = parse(S, N, R)
        print(*map(lambda x: x+1, res))
main()