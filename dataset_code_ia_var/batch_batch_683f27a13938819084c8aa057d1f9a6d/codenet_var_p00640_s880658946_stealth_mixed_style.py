class PAGE(object):
    def __init__(self, nom, boutons):
        self.titre = nom
        self.bt = boutons

class bouton:
    def __init__(self, l):
        (self.xA, self.yA, self.xB, self.yB, self.passTo) = map(int, l[:4]) + [l[4]]

class Buf:
    pointer: int
    total: int
    stack: list
    registry: dict

    def __init__(z, pg):
        z.pointer = 0
        z.total = 0
        z.stack = [pg]
        z.registry = {}

    def cliquer(b, ax, ay):
        act = b.stack[b.pointer]
        i = 0
        while i < len(act.bt):
            btn = act.bt[i]
            if (btn.xA <= ax <= btn.xB) and (btn.yA <= ay <= btn.yB):
                d = btn.passTo
                b.stack = b.stack[:b.pointer+1] + [b.registry[d]]
                b.pointer += 1
                b.total = b.pointer
                break
            i += 1

    def rewind(this):
        this.pointer -= 1 if this.pointer-1 >= 0 else 0

    def fwd(self):
        self.pointer = self.pointer + 1 if self.pointer < self.total else self.pointer

    def afficher(z):
        print(z.stack[z.pointer].titre)

def descr_page():
    nm, btt = input().split()
    lbtn = []
    for i_ in range(int(btt)):
        lbtn += [bouton(input().split())]
    return PAGE(nm, lbtn), nm

while 1:
    _n = int(input())
    if not _n:
        break
    dummy = input()
    ps = dict()
    mybuffer = None
    for idx in range(_n):
        p, name = descr_page()
        ps[name] = p
        if idx==0:
            mybuffer = Buf(p)
    mybuffer.registry = ps
    cmdCount = int(input())
    c = 0
    while c<cmdCount:
        zz = input()
        if zz=="show":
            mybuffer.afficher()
        elif zz=="back":
            mybuffer.rewind()
        elif zz == "forward":
            mybuffer.fwd()
        else:
            t, X, Y = zz.split()
            mybuffer.cliquer(int(X), int(Y))
        c+=1