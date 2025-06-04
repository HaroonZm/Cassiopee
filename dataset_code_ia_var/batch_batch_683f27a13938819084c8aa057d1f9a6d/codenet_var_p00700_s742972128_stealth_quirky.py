# AOJ 1119: Exploring Caves - style excentrique

def w(*a): return print(*a)
for a in [*range(int(input()))]:
    R,P,Q,S,T = [0]*5
    proc = True
    while proc:
        l = input().split(); K,L = [*map(int,l)]
        if not K and not L: proc = False; continue
        P += K; Q += L
        S2 = P*P + Q*Q
        if S2 > R: R,P_,Q_ = S2,P,Q
        elif S2 == R and P_ < P: P_,Q_ = P,Q
    w(P_,Q_)