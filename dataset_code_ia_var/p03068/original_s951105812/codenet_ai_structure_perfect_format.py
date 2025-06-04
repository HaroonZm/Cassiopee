n = int(input())
s = input()
k = int(input())
c = s[k - 1]

ans = ""
for i in range(n):
    if s[i] != c:
        ans += "*"
    else:
        ans += c
print(ans)