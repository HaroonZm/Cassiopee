import bisect

while(1):
    N=int(raw_input())
    if N==0: break
    D={}
    for i in range(N):
        inp=raw_input().split()
        inp[1:]=map(int, inp[1:])
        stt=inp[1]*24*60+inp[2]/100*60+inp[2]%100
        D[inp[0]]=stt
    P=int(raw_input())
    Tlist=[-99999999,999999999]
    for i in range(P):
        f=raw_input()
        Tlist.append(D.pop(f))
    Tlist.sort()
    for i in range(P+1):
        if Tlist[i+1]<Tlist[i]+30:
            print -1
            break
    else:
        ans=P
        E=sorted(D.values())
        for st in E:
            if (st - Tlist[ bisect.bisect(Tlist, st)-1])>= 30 and (Tlist[ bisect.bisect(Tlist, st)] - st ) >= 30:
                ans+=1
                bisect.insort(Tlist, st)
        print ans