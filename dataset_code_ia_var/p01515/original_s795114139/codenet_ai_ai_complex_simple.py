from itertools import product
import functools
import operator as op

def parse(S):
    S = f"{S}"
    V, O = [], []
    variables, op_priority = list("abcdefghijk"), {"-": 1, "+": 2, "*": 2, "@": 2}
    S = functools.reduce(lambda s, c: s.replace(c, f" {c} "), "()+-*@", S)
    rank, i = 0, 0
    annotate = lambda sym,i: ([-rank, op_priority[sym], i] if sym in op_priority else None)
    for s in S.split():
        rank += {"(":1, ")":-1}.get(s, 0)
        if s in variables + ["T","F"]: V.append(s); i += 1
        elif s not in "()" and s != " ": V.append(s); O.append(annotate(s,i)); i += 1
    G = [[] for _ in range(len(V))]
    P = [-1]*len(V)
    O = sorted(filter(None,O))
    follow = lambda k: follow(P[k]) if P[k] != -1 else k
    if O:
        for _,_,j in O:
            if V[j] == "-":
                d = follow(j+1)
                G[j].append(d); P[d]=j
            else:
                l,r = follow(j-1), follow(j+1)
                G[j]+=[l,r]; P[l]=P[r]=j
        p = P.index(-1)
    else:
        assert len(V) == 1; p = 0
    return G,V,p

def calculate(G,V,p,X):
    variables = set("abcdefghijk")
    ops = {
        "-": lambda i: not call(G[i][0]),
        "@": lambda i: not (call(G[i][0]) is True and call(G[i][1]) is False),
        "*": lambda i: call(G[i][0]) and call(G[i][1]),
        "+": lambda i: call(G[i][0]) or call(G[i][1])
    }
    def call(i):
        return (
            X.get(V[i], None) if V[i] in variables else
            {"T":True,"F":False}.get(V[i], None) if V[i] in "TF" else
            ops[V[i]](i) if V[i] in ops else
            (_ for _ in ()).throw(Exception("Unknown symbol"))
        )
    return call(p)

def truthtable(variables):
    return map(lambda values: dict(zip(variables, values)), product([True, False], repeat=len(variables)))

abc = list("abcdefghijk")
S = input()
while S != "#":
    L, R = map(lambda x: x.strip(), S.replace("->","@").split("="))
    def verdict():
        for X in truthtable(abc):
            eq = lambda side: calculate(*parse(side), X)
            if eq(L) != eq(R): return "NO"
        return "YES"
    print(verdict())
    S = input()