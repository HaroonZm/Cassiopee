ans = 0
s = input()
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        ans += 1
if ans:
    print("Yes")
else:
    print("No")