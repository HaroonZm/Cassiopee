import sys
input=sys.stdin.readline

N=int(input())
books=[]
for _ in range(N):
    t,a,d=input().rstrip().split()
    books.append((t,a,d))

Q=int(input())
for _q in range(Q):
    q_t,q_a,q_df,q_dt=input().rstrip().split()
    res=[]
    for t,a,d in books:
        if q_t!='*' and q_t not in t:
            continue
        if q_a!='*' and q_a not in a:
            continue
        if q_df!='*' and d<q_df:
            continue
        if q_dt!='*' and d>q_dt:
            continue
        res.append(t)
    if res:
        print('\n'.join(res))
    if _q!=Q-1:
        print()