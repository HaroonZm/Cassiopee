k, r = input().split()
k = int(k)
r = int(r)
if k >= 10:
    print(r)
else:
    print(r + 100 * (10 - k))