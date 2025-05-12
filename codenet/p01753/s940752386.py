eps = 1.0 / 10**10
def LI(): return [int(x) for x in input().split()]

def main():
    n,q = LI()
    na = [LI() for _ in range(n)]
    qa = [LI() for _ in range(q)]
    rr = []

    def k(a,b):
        return sum([(a[i]-b[i]) ** 2 for i in range(3)]) ** 0.5

    def f(a,b,c,r):
        ab = k(a,b)
        ac = k(a,c)
        bc = k(b,c)
        if ac <= r or bc <= r:
            return True
        at = (ac ** 2 - r ** 2) ** 0.5
        bt = (bc ** 2 - r ** 2) ** 0.5
        return ab >= at + bt - eps

    for x1,y1,z1,x2,y2,z2 in qa:
        tr = 0
        for x,y,z,r,l in na:
            if f((x1,y1,z1),(x2,y2,z2),(x,y,z),r):
                tr += l
        rr.append(tr)

    return '\n'.join(map(str,rr))

print(main())