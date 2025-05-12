c=[[0,0]]*6
for i in range(6):
    a,b=sorted(map(int,input().split()))
    c[i]=[a,b]
c.sort()
for i in range(0,6,2):
    if c[i]!=c[i+1]:print('no');break
else:print(['no','yes'][c[0][0]==c[2][0] and c[0][1]==c[4][0] and c[2][1]==c[4][1]])