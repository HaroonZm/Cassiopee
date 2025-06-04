n = int(input())
A = list(map(int, input().split()))
mn = A[0]
mx = A[0]
s = 0
for x in A:
    if x < mn:
        mn = x
    if x > mx:
        mx = x
    s += x
print(mn, mx, s)