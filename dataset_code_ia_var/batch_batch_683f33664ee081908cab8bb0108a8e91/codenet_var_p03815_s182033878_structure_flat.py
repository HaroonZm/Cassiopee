N = int(input())
ans = (N // 11) * 2
mod = N % 11
if mod == 0:
    pass
else:
    if mod <= 6:
        ans += 1
    else:
        ans += 2
print(ans)