a, b, x = [int(k) for k in input().split()]

if x >= a:
    d = ((x-b) // (a-b))* b + x
else:
    d = x

print(d%1000000007)