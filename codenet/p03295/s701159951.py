#ABC 103D回答
N,M=map(int,input().split())
A=[]
for i in range(M):
    a,b=map(int,input().split())
    A.append([a,b])
B=sorted(A,key=lambda x:x[1])
#print(B)
if M==0:
    print(0)
else:
    c=B[0][1]
    B.pop(0)
    count=1
    while B!=[]:
        if B[0][0]>=c:
            count=count+1
            c=B[0][1]
        B.pop(0)
        #print(B)
        #print(count)
    print(count)