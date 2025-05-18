N = int(input())
a = list(map(int,input().split()))
now = 0
for i in range(N):
    if a[i] % 4 == 0:
        now += 2
        continue
    if a[i] % 2 == 0:
        now += 1
if N%2 == 1:
    if now >= N-1:
        print("Yes")
    else:
        print("No")
else:
    if now >= N:
        print("Yes")
    else:
        print("No")