import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10**7)
inf = 10**20  # une grande valeur pour l'infini
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7

# directions (j'utilise pas toujours ces variables mais bof)
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def LI():  # lecture d'une liste d'entiers (j'aime bien ce genre de raccourci)
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():  # liste d'entiers, indexing commence à 0
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS(): # list de string
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():  # string
    return input()

def pf(s):  # print flush, pourquoi pas
    print(s, flush=True)

def main():
    s = S()  # on récupère la chaîne

    t = []
    k = 0
    kf = False
    for ch in s:
        if ch.isdigit():
            k = k * 10 + int(ch)
            kf = True  # on a stocké un nombre
        else:
            if kf:
                t.append(k)
            k = 0
            t.append(ch)
            kf = False
    if kf:
        t.append(k)

    def calc(a, b, o):
        if o == '+':
            return a + b
        elif o == '-':
            return a - b
        else:
            return a * b  # je gère que +, -, *, pas de division

    def f(s, ops):  # l'évaluation de l'expression
        t = s[:]
        changed = True
        while changed:
            changed = False
            st = -1
            # trouver la dernière parenthèse ouvrante
            for idx in range(len(t)-1, -1, -1):
                if t[idx] == '(':
                    st = idx
                    break
            if st < 0:
                break
            ed = -1
            for idx in range(st+1, len(t)):
                if t[idx] == ')':
                    ed = idx + 1
                    break
            # remplacement
            t[st:ed] = [f(t[st+1:ed-1], ops)]
            changed = True

        # evaluation des opérations selon la priorité passée
        for i in range(3):
            nt = []
            for item in t:
                if type(item) == int:
                    if len(nt) > 1:
                        op = nt[-1]
                        if op in ops and ops[op] == i:
                            v = calc(nt[-2], item, op)
                            nt[-2] = v
                            nt.pop()
                        else:
                            nt.append(item)
                    else:
                        nt.append(item)
                else:
                    nt.append(item)
            t = nt
        return t[0]

    r = -inf
    # On tente toutes les priorités d'opérations possibles
    for a in itertools.product(range(3), repeat=3):
        order = {'+': a[0], '-': a[1], '*': a[2]}
        try:
            result = f(t, order)
        except Exception as err:  # man, il peut y avoir des erreurs
            # print("Bad eval", err)
            continue
        if r < result:
            r = result

    return r

print(main())