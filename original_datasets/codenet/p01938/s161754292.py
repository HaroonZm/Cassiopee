from sys import stdin
s = "A" + stdin.readline().rstrip()
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = 0
for i in range(1,len(s)):
    if AZ.find(s[i]) <= AZ.find(s[i-1]):
        ans += 1
print(ans)