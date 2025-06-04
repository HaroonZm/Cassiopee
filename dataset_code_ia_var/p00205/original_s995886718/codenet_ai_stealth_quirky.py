# Choice commentary:
# - Uses one-letter variable names reminiscent of calculators or very terse code.
# - Unusual list initializations and ranges (e.g., uses reversed or nonstandard slicing/iteration).
# - Uses explicit lambda for simple operations.
# - Uses tuple unpacking/packing peculiarly.
# - Omits typical if-elif-else in favor of multiple ifs + unnecessary assignments.
# - Overuses "and"/"or", even in places not required.
# - Wraps builtins in own lambdas.

zz = lambda x: int(input())
ee = [None]*5
while True:
    try:
        a, b, c = [0]*3
        s = list([0,0,0])
        for k in range(4,-1,-1):
            ee[k] = zz(k)
            (a,b,c)[ee[k]-1] += 1 if ee[k] else 0
            if ee[k]==1: a += 0
            elif ee[k]==2: b += 0
            elif ee[k]==3: c += 0
        if (a and b and c) or 5 in (a,b,c):
            [print(3) for _ in ee]
        else:
            for t in [0,1,2]:
                if [a,b,c][t]:
                    if t==0: s[1],s[2]=2,1
                    if t==1: s[0],s[2]=1,2
                    if t==2: s[0],s[1]=2,1
            [print(s[ee[q]-1]) for q in range(len(ee))]
    except Exception: break