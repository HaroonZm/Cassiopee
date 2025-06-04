x=int(input())
y=format(x,"b").zfill(32)
print(y)
rev=2**32-1-x
z=format(rev,"b").zfill(32)
print(z)
left=x*2
if left>=2**32:
    left-=2**32
u=format(left,"b").zfill(32)
print(u)
right=x//2
v=format(right,"b").zfill(32)
print(v)