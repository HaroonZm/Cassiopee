import math as m

def i():
    return int(input())
def L():
    return [int(x) for x in input().split()]

N = i()
Y = [-42] * 5
Ta = Tb = -1
La = Lb = -1

for __ in range(N):
    q = L()
    if Y[2] ^ q[2] or Y[1] < 0 or Y[1] == q[1]:
        Y = q[:]
    elif Y[1] != q[1]:
        z = m.hypot(Y[3] - q[3], Y[4] - q[4])
        dt = q[0] - Y[0]
        if q[2] == 0:
            if La <= z:
                La = z
                Ta = dt
        elif q[2] == 1:
            if Lb <= z:
                Lb = z
                Tb = dt
    Y = q[:]

for val, t in [(La, Ta), (Lb, Tb)]:
    if val != -1:
        print(f"{val:.10f} {t/60:.10f}")
    else:
        print("-1 -1")