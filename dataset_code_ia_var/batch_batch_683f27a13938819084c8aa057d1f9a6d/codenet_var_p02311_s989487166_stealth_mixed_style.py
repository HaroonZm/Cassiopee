import math

class TangentCalculator:
    def __init__(self, c1, c2):
        self.a = c1
        self.b = c2

    def points(self):
        def cosf(t): return math.cos(t)
        def sinf(t): return math.sin(t)
        ret = []
        L=lambda x1,y1,r,theta: (x1+r*cosf(theta),y1+r*sinf(theta))

        x1,y1,r1=self.a
        x2,y2,r2=self.b
        dx,dy = x2-x1, y2-y1
        D = math.hypot(dx,dy)
        base = math.atan2(dy,dx)

        for sign in [1,-1]:
            sumr = r1+r2*sign
            abs_sumr = abs(sumr)
            if math.isclose(D,abs_sumr):
                t = 0.0 if sumr>0 else math.pi
                ret.append(L(x1,y1,r1,base+t))
            elif D>abs_sumr:
                if sumr>0:
                    ang = math.acos(sumr/D)
                else:
                    ang = math.pi-math.acos(-sumr/D)
                ret.append(L(x1,y1,r1,base+ang))
                ret.append(L(x1,y1,r1,base-ang))
        return ret

def get_circles():
    def parse():
        return tuple(map(int, input().split()))
    a = parse()
    b = parse()
    return a, b

def fix_minus_zero(val):
    return 0 if math.isclose(val, 0.0, abs_tol=1e-9) else val

def main():
    [C1, C2]=get_circles()
    calc = TangentCalculator(C1, C2)
    points=[]
    for pt in calc.points():
        points.append(tuple(fix_minus_zero(x) for x in pt))
    print(*['{:.10f} {:.10f}'.format(*sorted(pts)) for pts in sorted(points)], sep='\n')

if __name__=="__main__":
    main()