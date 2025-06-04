from string import digits
import sys

readline = sys.stdin.readline
write = sys.stdout.write

def parse(S, mp):
    M = 32768

    cur = 0  # Index in S

    # I think this does matrix transpose
    def transpose(m):
        p, q, v = m
        arr = [[0] * p for _ in range(q)]
        for i in range(q):
            for j in range(p):
                arr[i][j] = v[j][i]
        return q, p, arr

    # Looks for a submatrix
    def submatrix(m, a, b):
        p0, q0, v0 = m
        pa, qa, va = a
        pb, qb, vb = b
        assert pa == pb == 1  # Only row/col indexes
        va0 = va[0]
        vb0 = vb[0]
        arr = [[0] * qb for _ in range(qa)]
        for i in range(qa):
            e1 = va0[i]
            for j in range(qb):
                e2 = vb0[j]
                arr[i][j] = v0[e1-1][e2-1]
        return qa, qb, arr

    # Negating all elements, modulo M
    def neg(m0):
        p0, q0, v0 = m0
        res = [[0]*q0 for _ in range(p0)]
        for i in range(p0):
            for j in range(q0):
                res[i][j] = (-v0[i][j]) % M
        return p0, q0, res

    def emul(k, m):
        p, q, v = m
        arr = [[0]*q for _ in range(p)]
        for i in range(p):
            for j in range(q):
                arr[i][j] = k*v[i][j] % M
        return p, q, arr

    # Multiplies two matrices; or scales/left-multiplies by a number
    def mul(m0, m1):
        p0, q0, v0 = m0
        p1, q1, v1 = m1
        if p0 == q0 == 1:
            k0 = v0[0][0]
            if p1 == q1 == 1:
                k1 = v1[0][0]
                return 1, 1, [[k0 * k1]]
            return emul(k0, m1)
        elif p1 == q1 == 1:
            k1 = v1[0][0]
            return emul(k1, m0)
        assert q0 == p1
        arr = [[0]*q1 for _ in range(p0)]
        for i in range(p0):
            for j in range(q1):
                s = 0
                for k in range(q0):
                    s += v0[i][k]*v1[k][j]
                arr[i][j] = s % M
        return p0, q1, arr

    def add(m0, m1):
        p0, q0, v0 = m0
        p1, q1, v1 = m1
        assert p0 == p1 and q0 == q1
        arr = [[0]*q0 for _ in range(p0)]
        for i in range(p0):
            for j in range(q0):
                arr[i][j] = (v0[i][j] + v1[i][j]) % M
        return p0, q0, arr

    def sub(m0, m1):
        p0, q0, v0 = m0
        p1, q1, v1 = m1
        assert p0 == p1 and q0 == q1
        arr = [[0]*q0 for _ in range(p0)]
        for i in range(p0):
            for j in range(q0):
                arr[i][j] = (v0[i][j] - v1[i][j]) % M
        return p0, q0, arr

    # Parse matrix values, row by row
    def matrix():
        nonlocal cur
        cur += 1  # skip "["
        blocks = []
        r = 0
        while True:
            p, q, v = expr()
            blocks.append((r, 0, p, q, v))
            c = q
            while S[cur] == ' ':
                cur += 1  # skip space
                p1, q1, v1 = expr()
                blocks.append((r, c, p1, q1, v1))
                c += q1
            r += p
            if S[cur] == "]":
                break
            cur += 1  # skip ";"
        cur += 1  # skip "]"
        arr = [[0]*c for _ in range(r)]
        for r0, c0, p0, q0, v0 in blocks:
            for i in range(p0):
                for j in range(q0):
                    arr[r0+i][c0+j] = v0[i][j]
        return r, c, arr

    def number():
        nonlocal cur
        v = 0
        while S[cur] in digits:
            v = (v*10 + int(S[cur])) % M
            cur += 1
        return 1,1,[[v]]

    def factor():
        nonlocal cur
        sign = 0
        while S[cur] == "-":
            sign ^= 1
            cur += 1
        ch = S[cur]
        if ch == "(":
            cur += 1
            r = expr()
            cur += 1
        elif ch == "[":
            r = matrix()
        elif ch in digits:
            r = number()
        else:
            r = mp[ch]
            cur += 1  # advance after var

        while S[cur] in "('":
            if S[cur] == "'":
                t = 0
                while S[cur] == "'":
                    t ^= 1
                    cur += 1
                if t:
                    r = transpose(r)
            else:
                cur += 1  # (
                a = expr()
                cur += 1  # ,
                b = expr()
                cur += 1  # )
                r = submatrix(r, a, b)
        if sign:
            return neg(r)
        return r

    def term():
        nonlocal cur
        r = factor()
        # Maybe some exponentiation would be nice but well...
        while S[cur] == "*":
            cur += 1
            r1 = factor()
            r = mul(r, r1)
        return r

    def expr():
        nonlocal cur
        r = term()
        while S[cur] in "+-":
            op = S[cur]
            cur += 1
            r1 = term()
            if op == "+":
                r = add(r, r1)
            else:
                r = sub(r, r1)
        return r
    return expr()

def solve():
    N = int(readline())
    if N == 0:
        return False
    mp = {}
    for i in range(N):
        line = readline()
        v, s = line.strip().split("=")
        # Not stripping spaces for v, should be fine
        mp[v] = result = parse(s, mp)
        p, q, m = result
        for row in m:
            write(" ".join(str(x) for x in row))
            write("\n")
    write("-" * 5)
    write("\n")
    return True

while solve():
    pass  # Do... something? (not sure)