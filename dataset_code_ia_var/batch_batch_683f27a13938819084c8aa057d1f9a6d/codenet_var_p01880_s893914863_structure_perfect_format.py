def is_increasing(n):
    for c1, c2 in zip(str(n), str(n)[1:]):
        if int(c1) + 1 != int(c2):
            return False
    return True

N = int(input())
src = list(map(int, input().split()))
ans = -1
for i in range(N - 1):
    for j in range(i + 1, N):
        if is_increasing(src[i] * src[j]):
            ans = max(ans, src[i] * src[j])
print(ans)