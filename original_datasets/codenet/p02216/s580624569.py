N=int(input())
A=list(map(int,input().split()))

if N%2==1:
    if sum(A)%2==1:
        print("First")
    else:
        print("Second")
else:
    if min(A)%2==1:
        print("First")
    else:
        if sum(A)%2==0:
            print("Second")
        else:
            print("First")