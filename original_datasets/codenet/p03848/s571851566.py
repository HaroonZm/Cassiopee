import collections
n = int(input())
a = list(map(int,input().split()))
c = collections.Counter(a)
p = sorted(c.items())
ans = 1
if n % 2 == 0:
    for i in range(n//2):
        if p[i][0] != 2*i+1 or p[i][1] != 2:
            print(0)
            exit()
elif n % 2 == 1:
    for i in range(n//2 + 1):
        if i == 0:
            if p[i][0] != 0 or p[i][1] != 1:
                print(0)
                exit()
        elif p[i][0] != 2*i or p[i][1] != 2:
            print(0)
            exit()

print((2**(n//2))%(10**9+7))