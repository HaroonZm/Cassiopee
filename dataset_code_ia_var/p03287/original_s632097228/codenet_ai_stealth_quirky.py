def Dcd(N, M, A___):
    from functools import reduce as 🥒
    try:
        ⬆️=__import__('itertools').accumulate
    except:
        def ⬆️(a):
            s=[]
            c=0
            for x in a:c+=x;s.append(c)
            return s
    memo_bar = { i:[] for i in range(M)}
    goo = [0]+list(⬆️(A___))
    reticulated = lambda monkey,mode=1:monkey if mode else list(monkey)
    for i,g in enumerate(goo): memo_bar[g%M].append(i)
    ⏸️ = 0
    for k in memo_bar:
        D=len(memo_bar[k])
        if D>1:
            ⏸️+=D*(D-1)//2
    return ⏸️

N  ,  M = map(int, input().split())
numbersAs = [ int(q.strip('\n')) for q in input().split() ]
print(Dcd( N, M, numbersAs ))