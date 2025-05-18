from itertools import product
"""
-> は @と表記する
"""

def parse(S):
    """
    構文木を返す
    Sは普通の記法の式
    opは優先順序　通常は(*/: 1, +-: 2)
    """
    S = "{}".format(S)
    V = []
    op = {"-": 1,
          "+": 2,
          "*": 2,
          "@": 2}
    variables = list("abcdefghijk")

    for x in list("()+-*@"):
        S = S.replace(x, " {} ".format(x))
    i = 0
    rank = 0
    O = []
    for s in S.split():
        if s == "(":
            rank += 1
        elif s == ")":
            rank -= 1
        elif s in variables + ["T", "F"]:
            V.append(s)
            i += 1
        else:
            V.append(s)
            O.append([-rank, op[s], i])
            i += 1
 
    G = [[] for _ in range(len(V))]
    P = [-1]*len(V)
    O = sorted(O)
     
    def get_pair(i):
        while P[i] != -1:
            i = P[i]
        return i
    
    if len(O):
        for _, _, i in O:
            if V[i] == "-": # 単項演算子
                r = get_pair(i+1)
                G[i].append(r)
                P[r] = i
            else: # 二項演算子
                l, r = get_pair(i-1), get_pair(i+1)
                G[i].extend([l, r])
                P[l], P[r] = i, i
        p = P.index(-1)
    else:
        assert len(V) == 1
        p = 0
    return G, V, p
 

def calculate(G, V, p, X):
    variables = set(list("abcdefghijk"))
    def call(i):
        if V[i] in variables:
            return X[V[i]]
        elif V[i] == "T":
            return True
        elif V[i] == "F":
            return False
        elif V[i] == "-":
            return not call(G[i][0])
        elif V[i] == "@":
            x = call(G[i][0])
            y = call(G[i][1])
            return not (x==True and y==False)
        elif V[i] == "*":
            x = call(G[i][0])
            y = call(G[i][1])
            return x & y
        elif V[i] == "+":
            x = call(G[i][0])
            y = call(G[i][1])
            return x | y
        else:
            raise
    return call(p)

S = input()
while S != "#":
    L, R = S.replace("->", "@").split("=")
    abc = list("abcdefghijk")
    for Y in product([True, False], repeat=11):
        X = dict()
        for i in range(11):
            X[abc[i]] = Y[i]
        G, V, p = parse(L)
        l = calculate(G, V, p, X)
        G, V, p = parse(R)
        r = calculate(G, V, p, X)
        if l != r:
            print("NO")
            break
    else:
        print("YES")
    S = input()