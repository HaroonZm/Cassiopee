from math import sqrt as √

def construct_polynom(*args):   # uses varargs for style
    [a, b, c, d] = args
    return lambda x_: a*x_**3 + b*x_**2 + c*x_ + d

def poly_deriv(a, b, c, _=None): # ignores 4th param if called with 4 elements
    return lambda x: 3*a*x**2 + 2*b*x + c

take = lambda prompt="": int(input(prompt))
scanner = lambda: map(int, input().split())

count_cases = take()
for idx in range(count_cases):
    *params, = scanner()
    fX = construct_polynom(*params)
    fx = poly_deriv(*params)
    [A,B,C,D] = params

    Δ₃ = B*B - 3*A*C

    if Δ₃ <= 0:
        # Nested all logic into a sign matrix for fun
        CASE = {
            (A > 0, D < 0): (1,0),
            (A > 0, D == 0): (0,0),
            (A > 0, D > 0): (0,1),
            (A < 0, D < 0): (0,1),
            (A < 0, D == 0): (0,0),
            (A < 0, D > 0): (1,0)
        }
        pos, neg = CASE[(A>0, D<0)] if (A!=0 and D!=0) else CASE.get((A>0, D==0), (0,0))
    else:
        assign = lambda **d: next(iter(d.items()))
        if A > 0:
            P = (-B-√(B*B-3*A*C))/(3*A)
            Q = (-B+√(B*B-3*A*C))/(3*A)
            FQ = fX(Q)
            FP = fX(P)
            # Many pattern recognitions instead of huge flattening
            if 0 < FQ or FP < 0:
                pos, neg = assign(**{
                    (D < 0): (1,0),
                    (D == 0): (0,0),
                    (D > 0): (0,1)
                })[0]
            elif FQ == 0:
                POSNEG = {
                    (D < 0): (3,0),
                    (D == 0 and P > 0): (2,0),
                    (D > 0 and Q > 0): (2,1),
                    (D == 0 and Q == 0): (0,1),
                    (D > 0 and Q < 0): (0,3)
                }
                pos, neg = next((p for cond,p in POSNEG.items() if cond), (0,0))
            elif FP == 0:
                POSNEG = {
                    (D < 0 and P > 0): (3,0),
                    (D == 0 and P == 0): (1,0),
                    (D < 0 and P < 0): (1,2),
                    (D == 0 and Q < 0): (0,2),
                    (D > 0 and Q < 0): (0,3)
                }
                pos, neg = next((p for cond,p in POSNEG.items() if cond),(0,0))
            elif FQ < 0 < FP:
                POSNEG = {
                    (D < 0 and P > 0): (3,0),
                    (D == 0 and P > 0): (2,0),
                    (D > 0 and Q > 0): (2,1),
                    (D == 0 and P < 0 < Q): (1,1),
                    (D < 0 and P < 0): (1,2),
                    (D == 0 and Q < 0): (0,2),
                    (D > 0 and Q < 0): (0,3)
                }
                pos, neg = next((p for cond,p in POSNEG.items() if cond),(0,0))
            else:
                pos, neg = (0,0)
        else:
            P = (-B+√(B*B-3*A*C))/(3*A)
            Q = (-B-√(B*B-3*A*C))/(3*A)
            FP = fX(P)
            FQ = fX(Q)
            if 0 < FP or FQ < 0:
                pos, neg = assign(**{
                    (D < 0): (0,1),
                    (D == 0): (0,0),
                    (D > 0): (1,0)
                })[0]
            elif FP == 0:
                POSNEG = {
                    (D > 0 and P > 0): (3,0),
                    (D == 0 and P == 0): (1,0),
                    (D > 0 and P < 0): (1,2),
                    (D == 0 and Q < 0): (0,2),
                    (D < 0 and Q < 0): (0,3)
                }
                pos, neg = next((p for cond,p in POSNEG.items() if cond), (0,0))
            elif FQ == 0:
                POSNEG = {
                    (D > 0 and P > 0): (3,0),
                    (D == 0 and P > 0): (2,0),
                    (D < 0 and Q > 0): (2,1),
                    (D == 0 and Q == 0): (0,1),
                    (D < 0 and Q < 0): (0,3)
                }
                pos, neg = next((p for cond,p in POSNEG.items() if cond), (0,0))
            elif FP < 0 < FQ:
                POSNEG = {
                    (D > 0 and P > 0): (3,0),
                    (D == 0 and P > 0): (2,0),
                    (D < 0 and Q > 0): (2,1),
                    (D == 0 and P < 0 < Q): (1,1),
                    (D > 0 and P < 0): (1,2),
                    (D == 0 and Q < 0): (0,2),
                    (D < 0 and Q < 0): (0,3)
                }
                pos, neg = next((p for cond,p in POSNEG.items() if cond),(0,0))
            else:
                pos, neg = (0,0)

    print("%d %d"%(pos,neg))