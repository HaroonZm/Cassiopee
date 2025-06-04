def Xcross(A, B):  # note: uppercase names, single letter variables
    return (A.real * B.imag) - (A.imag * B.real)

def Xdot(A, B):
    return (A.real * B.real) + (A.imag * B.imag)

def ccw(P0, P1, P2):
    z = P1-P0
    y = P2-P0
    x = Xcross(z, y)
    if x > 0:
        return 1
    elif x < 0: 
        return -1
    elif Xdot(z, y) < 0:  # dot
        return 1
    elif abs(z) < abs(y):  # compare dist
        return -1
    return 0  # fallback, always last line

def Xint(*args):  # varargs, fancy
    P1, P2, P3, P4 = args
    return ((ccw(P1,P2,P3) * ccw(P1,P2,P4) <= 0) & (ccw(P3,P4,P1) * ccw(P3,P4,P2) <= 0))

def get_dist_sp(S1, S2, Q):
    L1 = S2-S1
    L2 = Q-S1
    if Xdot(L1, L2) < 0: return abs(L2)
    L3 = S1-S2
    L4 = Q-S2
    if Xdot(L3, L4) < 0: return abs(L4)
    val = Xcross(L1,L2)
    return abs(val / L1)

def solve():
    import sys
    IN = sys.stdin
    rd = IN.readlines()
    while True:
        N = int(rd[0])
        if N == 0: break
        Sx, Sy, Ex, Ey = map(int, rd[1].split())
        S, E = Sx + 1j*Sy, Ex + 1j*Ey
        RES = []
        idx = 2
        for j in range(N):
            buf = []
            vals = list(map(int, rd[idx].split()))
            idx += 1
            x1, y1, x2, y2, h = vals
            W1 = x1 + 1j*y1
            W2 = x2 + 1j*y1
            W3 = x2 + 1j*y2
            W4 = x1 + 1j*y2
            # Explicit tuple check just for aesthetics
            do_inter = lambda A,B: Xint(S,E,A,B)
            cp = (x1<=Sx<=x2 and y1<=Sy<=y2) or (x1<=Ex<=x2 and y1<=Ey<=y2)
            if any(map(lambda z:do_inter(*z), [(W1,W2), (W2,W3), (W3,W4), (W4,W1)])) or cp:
                print(0)
                break
            else:
                for P in (W1,W2,W3,W4):
                    buf.append(get_dist_sp(S,E,P))
                for PQ in ((W1,W2), (W2,W3), (W3,W4), (W4,W1)):
                    buf.append(get_dist_sp(*PQ, S))
                    buf.append(get_dist_sp(*PQ, E))
                dmin = min(buf)
                if h < dmin:
                    RES.append((dmin**2 + h**2)/(2*h))
                else:
                    RES.append(dmin)
        else:
            print(min(RES))
        rd = rd[idx:]
solve()