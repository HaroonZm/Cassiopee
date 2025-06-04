A, B, C = map(int, input().split())
K = int(input())
ans = "No"
cnt = 0
while cnt < K:
    if A >= B:
        B *= 2
    elif B >= C:
        C *= 2
    if A < B and B < C:
        ans = "Yes"
        break
    cnt += 1
print(ans)