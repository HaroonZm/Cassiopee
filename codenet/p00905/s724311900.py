import re
while 1:
    R=[]
    C=[]
    S=[]
    p,q=map(int,input().split())
    if p==q==0:break
    #P=[input()for _ in range(p)]
    G=[]
    R_c=[0]
    C_c=[0]
    S_c=[0]
    for _ in range(p):
        s=input()
        cnt=s.count
        G.append(re.match('[.]*',s).span()[1])
        R_c.append(R_c[-1]+cnt('(')-cnt(')'))
        C_c.append(C_c[-1]+cnt('{')-cnt('}'))
        S_c.append(S_c[-1]+cnt('[')-cnt(']'))
    for x in range(1,21):
        for y in range(1,21):
            for z in range(1,21):
                for g,i,j,k, in zip(G,R_c,C_c,S_c):
                    if i*x+j*y+k*z!=g:
                        break
                else:
                    R.append(x)
                    C.append(y)
                    S.append(z)
    #print(R,C,S)
    R_c=[0]
    C_c=[0]
    S_c=[0]
    for _ in range(q):
        s=input()
        cnt=s.count
        R_c.append(R_c[-1]+cnt('(')-cnt(')'))
        C_c.append(C_c[-1]+cnt('{')-cnt('}'))
        S_c.append(S_c[-1]+cnt('[')-cnt(']'))
    R_c=R_c[:-1]
    C_c=C_c[:-1]
    S_c=S_c[:-1]

    a=[set()for _ in range(q)]
    for x,y,z in zip(R,C,S):
        for idx,(i,j,k)in enumerate(zip(R_c,C_c,S_c)):
            a[idx].add(i*x+j*y+k*z)
    print(*[list(t)[0]if len(t)==1else-1for t in a])