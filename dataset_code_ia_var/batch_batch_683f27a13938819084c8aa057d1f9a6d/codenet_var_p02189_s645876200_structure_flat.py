N = int(input())
a = list(map(int, input().split()))
mina = a[0]
ans = 0
i = 1
while i < N:
    if a[i] < mina:
        mina = a[i]
        ans = i
    i += 1
print(ans + 1)