def sign(p1,p2,p3):
    return (p1[0]-p3[0])*(p2[1]-p3[1])-(p2[0]-p3[0])*(p1[1]-p3[1])
def check(triangle,pt):
    v1=[triangle[0],triangle[1]]
    v2=[triangle[2],triangle[3]]
    v3=[triangle[4],triangle[5]]
    b1=sign(pt,v1,v2)
    flag1=1 if b1>0 else 0
    b2=sign(pt,v2,v3)
    flag2=1 if b2>0 else 0
    b3=sign(pt,v3,v1)
    flag3=1 if b3>0 else 0
    return (flag1==flag2) and (flag2==flag3)
n=int(input())
for _ in range(n):
    query=list(map(int,input().split()))
    triangle=query[0:6]
    hikoboshi=query[6:8]
    orihime=query[8:10]
    check1=check(triangle,hikoboshi)
    check2=check(triangle,orihime)
    if check1==check2:
        print("NG")
    else:
        print("OK")