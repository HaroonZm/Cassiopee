N = int(input())
S = input()

ans = 0
l = 0
r = 1

while l < N and r < N:
    found = False
    length = r - l
    first_sub = S[l:r]
    for k in range(l + length, N - length + 1):
        second_sub = S[k:k + length]
        if first_sub == second_sub:
            ans = max(ans, length)
            found = True
            break
    if found and r < N - 1:
        r += 1
    else:
        l += 1
        r = min(r + 1, N - 1)

print(ans)