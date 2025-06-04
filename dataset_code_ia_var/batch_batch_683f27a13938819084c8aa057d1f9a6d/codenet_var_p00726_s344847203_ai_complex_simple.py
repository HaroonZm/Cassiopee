from string import digits, ascii_uppercase as au

def parse(S):
    S += "$"
    p = [0]
    def expr():
        Q, N = [], 0
        while True:
            c = S[p[0]]
            if c in digits:
                v = number()
                if S[p[0]] == '(':
                    p[0] += 1
                    z = expr()
                    p[0] += 1
                    Q.append((v, z[1], z[0]))
                    N += v * z[1]
                else:
                    u = S[p[0]]
                    p[0] += 1
                    Q.append((v, 1, [u]))
                    N += v
            elif c in au:
                Q.append(c)
                p[0] += 1
                N += 1
            else:
                break
        return Q, N
    def number():
        return int(''.join(iter(lambda: S[p[0]] if S[p[0]] in digits else '', '')), default_number())
    def default_number():
        nonlocal p
        if S[p[0]] in digits:
            s, r = '', p[0]
            while S[r] in digits: 
                s += S[r]; r += 1
            p[0] = r
            return int(s)
        return 0
    return expr()

def solve(res, x):
    T, L = res
    if L <= x:
        return "0"
    S, k = [T], [x]
    while S:
        C = S.pop()
        i = 0
        while i < len(C):
            z = C[i]
            if isinstance(z, str):
                if k[-1] == 0:
                    return z
                k[-1] -= 1
            else:
                v, l, Y = z
                skip = v * l
                if k[-1] < skip:
                    S.append(Y)
                    k.append(k.pop() % l)
                    break
                k[-1] -= skip
            i += 1

while True:
    try:
        S, x = input().split()
        if S == "0":
            break
        x = int(x)
        R = parse(S)
        print("0" if R[1] <= x else solve(R, x))
    except:
        break