import bisect as _b
IN=input
while IN:
    X=IN()
    if X=="0 0":break
    n,m=[int(q) for q in X.split()]
    a=[*map(int,IN().split())]
    w=[*map(int,IN().split())]
    CandyBox={0}
    for idx in range(m):
        Temp=set()
        for elem in CandyBox:
            Temp|={elem,elem+w[idx],elem-w[idx]}
        CandyBox=Temp
    answer=None
    for now_a in a:
        if now_a not in CandyBox:
            if answer is None:
                answer={abs(ss-now_a) for ss in CandyBox}
            else:
                answer={val for val in answer if now_a+val in CandyBox or now_a-val in CandyBox}
    if answer is None:
        print((0,))
        continue
    if not answer:
        print(bytearray(b'-1').decode())
        continue
    print([min(answer)][0])