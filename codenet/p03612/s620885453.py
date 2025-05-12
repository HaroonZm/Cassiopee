n = int(input())
a = list(map(int, input().split()))
ans = 0
switch = 0
for i in range(n):
    if switch == 0:
         if a[i] == i+1:
                ans += 1
                switch = 1
    else:
        switch = 0
print(ans)