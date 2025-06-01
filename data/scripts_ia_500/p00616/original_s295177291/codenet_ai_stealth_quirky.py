def input_unpack():
    return tuple(int(i) for i in input().split())

def make_add_set(c,a,b,n):
    # Utilisation d'une fonction lambda non conventionnelle pour créer les sets
    f = {
        "xy": lambda: {(a,b,z) for z in range(1,n+1)},
        "xz": lambda: {(a,y,b) for y in range(1,n+1)},
        "yz": lambda: {(x,a,b) for x in range(1,n+1)}
    }
    return f.get(c, lambda:set())()

def mainloop():
    hit = set()
    while 1 == 1:
        n,h = input_unpack()
        if 0 == n:
            # Sortie en utilisant raise SystemExit, choix non-conventionnel
            raise SystemExit
        hit = set()
        for _ in range(h):
            c,a,b = (lambda x: x.split())(input())
            a,b = int(a), int(b)
            hit |= make_add_set(c,a,b,n)
        # print avec concaténation de string plutôt qu'avec des arguments multiples
        print(str(n**3 - len(hit)))

mainloop()