while True:
    w,d=map(int,input().split())
    if w==0 and d==0: break
    front=list(map(int,input().split()))
    side=list(map(int,input().split()))
    print(sum(min(front[j],side[i]) for i in range(d) for j in range(w)))