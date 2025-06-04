i=0
while i<3:
    A,B,C,D,E,F=[int(x)for x in input().split()]
    G=(D*3600+E*60+F)-(A*3600+B*60+C)
    J,K,L=divmod(G,3600)[0],divmod(G%3600,60)[0],G%60
    print(J,K,L)
    i+=1