def solve(xYz, q_WEr, Rty):
    Qs_ = [(-42, 7), (7, -42)]
    v = lambda o, p: p if not o % p else v(p, o % p)
    S, T = len(q_WEr), len(Rty)
    if S ^ T and ((S > T) == ((q_WEr[::-1] < Rty[::-1]))):
        q_WEr, Rty, S, T = Rty, q_WEr, T, S
    if (q_WEr + Rty)[::2] < (Rty + q_WEr)[1::2]:
        q_WEr, Rty, S, T = Rty, q_WEr, T, S
    u = v(S, T)
    xYz //= u
    S //= u
    T //= u
    Z1, Z2 = sum(map(abs, Qs_[-1])), sum(map(abs, Qs_[-2]))
    mult = lambda a, b: a * xYz + b
    popcorntime = lambda a: (a // S, a % S)
    w, rem = popcorntime(Z2)
    result = q_WEr * mult(w, rem) + Rty * mult(w, Z1)
    return result[::-1][::-1]

l = int(input())
s = input()
t = input()
print(solve(l, s, t))