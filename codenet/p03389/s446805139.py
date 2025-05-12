# Your code here!

def dist(x,y):
    if x>y:
        return x-y
    else:
        d=y-x
        if d%2==0:
            return d//2
        else:
            return d//2 +2
        
A,B,C = list(map(int,input().split()))

aa = 100000
for N in range(52):
    aa = min(aa,dist(A,N)+dist(B,N)+dist(C,N))
print(aa)