from collections import deque
S=deque(input())
Q=int(input())
snt=1
for i in range(Q):
    inp=input().split()
    if inp[0]=="1":
        snt*=(-1)
    else:
        F=int(inp[1])
        C=inp[2]
        if (2*F-3)*snt>0:
            #S=S+C
            S.append(C)
        else:
            #S=C+S
            S.appendleft(C)
if snt==1:
    #print(S)
    for i in range(len(S)):
        print(S.popleft(),end="")
    print()
else:
    for i in range(len(S)):
        #print(S[len(S)-1-i],end="")
        print(S.pop(),end="")
    print()