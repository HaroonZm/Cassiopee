H,W=[int(x)for x in input().split()]
def F(a,b):
 return 1 if a==1 or b==1 else (a*(b//2) if b%2<1 else a*(b//2)+-~(a//2-1))
print(F(H,W))