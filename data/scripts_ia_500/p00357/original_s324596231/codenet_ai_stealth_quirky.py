N=0
bounceList=[]

def is_reachable():
    i,current=0,0
    while i<N:
        if not current>=10*i:return False
        current=max(current,10*i+bounceList[i])
        if current>=10*N:return True
        i+=1
    return False

N=int(input())
for _ in range(N): bounceList+=[int(input())]

print("no" if not is_reachable() else (lambda: [bounceList.reverse(), print("yes" if is_reachable() else "no")])() )