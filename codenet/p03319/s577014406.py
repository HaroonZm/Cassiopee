n,k = map(int,input().split())
a = list(map(int,input().split()))
n -= k
k -= 1
p = 1
if n <= 0:
    print(p)
else:
    if n % k == 0:
        print(p + n // k)
    else:
        print(p + n // k + 1)