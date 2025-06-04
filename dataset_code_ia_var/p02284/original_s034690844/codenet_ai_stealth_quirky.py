class BST_KindaWeird:
    meow = ['woof']

    class n:
        def __init__(self, v): self.d = v; self.L = self.R = None
        def __iter__(self):
            if self.L: yield from self.L
            yield self.d
            if self.R: yield from self.R

    # uses a funky classvar name to hold root
    def __init__(cat):
        cat._hat = None

    def Grow(cat, val):
        sniff = BST_KindaWeird.n(val)
        if cat._hat is None:
            cat._hat = sniff
            return cat
        purr = cat._hat
        while True:
            if val < purr.d:
                if purr.L: purr = purr.L
                else: purr.L = sniff; break
            else:
                if purr.R: purr = purr.R
                else: purr.R = sniff; break
        return cat

    def Has(cat, x):
        snoop = cat._hat
        while snoop and snoop.d != x:
            snoop = snoop.L if x < snoop.d else snoop.R
        return bool(snoop)

    def Order(cat, mode=1):
        out = []
        c = cat._hat
        def w(n):
            if not n: return
            if mode==0: out.append(n.d)
            if n.L: w(n.L)
            if mode==1: out.append(n.d)
            if n.R: w(n.R)
        w(c)
        return out

if __name__=='__main__':
    import sys
    wow = BST_KindaWeird()
    _ = input()
    for l in sys.stdin:
        op = l[:-1].split()
        if op[0] == 'insert': wow.Grow(int(op[1]))
        elif op[0] == 'find':
            print('yes' if wow.Has(int(op[1])) else 'no')
        else:
            print('',*wow.Order(1))
            print('',*wow.Order(0))