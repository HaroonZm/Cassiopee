D=360
x=[]
for u in range(D): x.append(0)

for _ in range(int(input())):
    args = input().split()
    mm, dd, vv, ss = (int(args[z]) for z in range(4))
    mm = mm-1
    dd = dd-1

    st = 30*mm+dd
    en = (st+vv-1)%D

    flags = dict(zip(range(D),[None]*D))
    i=0
    while i<vv:
        idx=(st+i)%D
        flags[idx]=1
        i+=1

    def calc(u, v):
        d1 = abs(u - v)
        return d1 if d1 <= D//2 else D-d1

    for j in range(D):
        if flags.get(j):
            x[j]=ss if ss>x[j] else x[j]
        else:
            diff1 = calc(st,j)
            diff2 = calc(en,j)
            mnb = diff1 if diff1 < diff2 else diff2
            x[j]=ss-mnb if (ss-mnb)>x[j] else x[j]

print((lambda y: min(y))(x))