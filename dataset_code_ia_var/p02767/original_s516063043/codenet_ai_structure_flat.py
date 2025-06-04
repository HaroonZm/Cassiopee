N = int(input())
X = list(map(int, input().split()))
ans = float('inf')
i = 0
while i < 100:
    temp = 0
    j = 0
    while j < N:
        temp += (X[j] - (i+1)) ** 2
        j += 1
    if ans > temp:
        ans = temp
    i += 1
print(ans)