while True:
    n,p=map(int,input().split())
    if n==0 and p==0:
        break
    bowl=p
    kept=[0]*n
    current=0
    steps=0
    while True:
        steps+=1
        if bowl>0:
            bowl-=1
            kept[current]+=1
            if bowl==0 and sum(kept)-kept[current]==0:
                print(current)
                break
        else:
            bowl=sum(kept)
            kept=[0]*n
        current=(current-1)%n