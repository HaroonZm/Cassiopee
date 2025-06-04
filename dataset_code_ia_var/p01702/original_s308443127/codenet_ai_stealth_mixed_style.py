from functools import reduce

def get_input():
    return list(map(int, input().split()))

def make_table():
    chars = []
    for i in range(10):
        chars.append(str(i))
    letters = ""
    for i in range(26):
        letters += chr(ord("A") + i)
    return "".join(chars) + letters

def singleton(c):
    if len(c) == 1:
        (x,) = c
        return x
    return None

def do_query(n, m, q, ops):
    legit = [{i for i in range(n)} for _ in range(m)]
    prev=None
    for cnt, (s, b) in enumerate(ops):
        slist = list(map(int, s))
        blist = list(map(int, b))
        if prev is not None:
            slist = list(map(lambda ab: ab[0]^ab[1], zip(slist, prev)))
        z0 = set()
        o1 = set()
        for idx, val in enumerate(slist):
            if val == 0: z0.add(idx)
            elif val == 1: o1.add(idx)
        for z in range(m):
            legit[z] = legit[z] - o1 if blist[z]==0 else legit[z]
            legit[z] = legit[z] - z0 if blist[z]==1 else legit[z]
        prev = slist
    return legit

def print_result(legit, table):
    c = 0
    while c<len(legit):
        v = legit[c]
        if sum(1 for _ in v)==1:
            print(table[list(v)[0]], end="")
        else:
            print("?", end="")
        c += 1
    print()

while True:
    x = get_input()
    if not any(x): break
    n, m, q = x
    data = []
    i = 0
    while i < q:
        tmp = input().split()
        data.append((tmp[0], tmp[1]))
        i += 1
    table = make_table()
    legit = do_query(n, m, q, data)
    print_result(legit, table)