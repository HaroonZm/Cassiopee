from sys import stdin as Q;P=lambda:map(int,Q.readline().split())
n=int(Q.readline())
r=[]
for _ in range(n):r.append((int(Q.readline()), 'A'))
for _ in range(n):r.append((int(Q.readline()), 'B'))
magic=10**9+7

m=1
ct={'A':0,'B':0}
r.sort(key=lambda u:u[0])
i=0
while i<len(r):
    a,b=r[i]
    if b=='A':
        if ct['B']:
            m=(m*ct['B'])%magic
            ct['B']-=1
        else:
            ct['A']+=1
    else:
        if ct['A']:
            m=(m*ct['A'])%magic
            ct['A']-=1
        else:
            ct['B']+=1
    i+=1
print(m)