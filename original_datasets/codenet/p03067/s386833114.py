A,B,C=map(int,input().split())
A,B=sorted([A,B])
if C in [i for i in range(A,B)]:
    print("Yes")
else:
    print("No")