n=[i+1 for i in range(30)]
i=0
while i<28:
    v=int(input())
    idx=n.index(v)
    n.pop(idx)
    i+=1
print(*n,sep='\n')