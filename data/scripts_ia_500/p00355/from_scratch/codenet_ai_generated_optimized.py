a,b=map(int,input().split())
N=int(input())
intervals=[tuple(map(int,input().split())) for _ in range(N)]
for s,f in intervals:
    if not (b<=s or a>=f):
        print(1)
        break
else:
    print(0)