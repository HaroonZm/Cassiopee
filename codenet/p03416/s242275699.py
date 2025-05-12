A,B=map(int,input().split())
num=0
for i in range(A,B+1):
    N=str(i)
    if N==N[::-1]:
        num+=1
print(num)