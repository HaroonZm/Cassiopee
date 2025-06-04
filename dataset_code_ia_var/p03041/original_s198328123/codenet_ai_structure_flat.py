n, k = map(int, input().split())
s = input()
ans = ""
i = 0
while i < n:
    if i == k - 1:
        ans += s[i].lower()
    else:
        ans += s[i]
    i += 1
print(ans)