n = int(input())
t, a = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]

h_ = [t - x*0.006 for x in h]

ans = 0
d = float('inf')
for i,x in enumerate(h_):
    d_ = abs(a - x)
    if d > d_:
        d = d_
        ans = i+1

print(ans)