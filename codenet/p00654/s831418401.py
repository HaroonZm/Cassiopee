import math

while(1):
    n=int(raw_input())
    if n==0:    break
    A=map(int,raw_input().split())
    E=[]
    D=[]
    for a in A:
        if a%2==0:
            E.append(a)
        else:
            D.append(a)
    E.sort()
    D.sort()
    
    g=2
    el=E[0]
    for i in range(100):
        if el>>i%2:
            g**=i
            break
    E=[e/g for e in E]
    
    k1=int(math.sqrt(D[0]*E[0]/E[1]))
    ga =E[0]/k1
    E=[e/ga for e in E]
    
    print int(g*ga)
    print ' '.join(map(str,map(int,E)))