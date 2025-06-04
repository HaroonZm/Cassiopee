N,A,B=[*map(int,input().split())]
S=input()
total,foreign=0,0
X=lambda q:print(q)
for idx,ch in enumerate(S):
    if ch=="a":
        if total<A+B:
            X("Yes");total+=1
        else:X("No")
    elif ch=="b":
        if total<A+B and foreign<B:
            X("Yes");total+=1;foreign+=1
        else:X("No")
    else:X("No")