from itertools import product

def parse(S, op):
    """
    構文木を返す
    Sは普通の記法の式
    opは優先順序　通常は(*/: 1, +-: 2)
    """
    S = "0+({})".format(S)
    V = []
    for x in list("()+-*"):
        S = S.replace(x, " {} ".format(x))
    i = 0
    rank = 0
    O = []
    for s in S.split():
        if s == "(":
            rank += 1
        elif s == ")":
            rank -= 1
        elif s.isdigit():
            V.append(s)
            i += 1
        else:
            V.append(s)
            O.append([-rank, op[s], i])
            i += 1
    G = [[] for _ in range(len(V))]
    P = [-1] * len(V)
    O = sorted(O)
    def get_pair(i):
        while P[i] != -1:
            i = P[i]
        return i
    for _, _, i in O:
        l, r = get_pair(i - 1), get_pair(i + 1)
        G[i].extend([l, r])
        P[l], P[r] = i, i
    p = O[-1][2]
    return G, V, p

def make(G, V, p):
    def call(i):
        if V[i].isdigit():
            return V[i]
        else:
            assert len(G[i]) == 2
            left = call(G[i][0])
            right = call(G[i][1])
            return "({}{}{})".format(left, V[i], right)
    return call(p)

S = input()
ans = -float("inf")
for a, b, c in product(range(3), repeat=3):
    op = {}
    op["+"] = a
    op["-"] = b
    op["*"] = c
    ans = max(ans, eval(make(*parse(S, op))))
print(ans)