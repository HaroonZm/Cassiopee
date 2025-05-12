N = int(input())
a = [int(x) for x in input().split()]
min_a = min(a)
max_a = max(a)
ans = 10**10
for i in range(min_a,max_a+1):
    sum_c = 0
    for x in a:
        sum_c += (x-i)**2
    ans = min(ans,sum_c)
print(ans)