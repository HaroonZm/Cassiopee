def check(t, s):
    count = 0
    for i in range(len(t)):
        if s[i] != t[i]:
            count += 1
    return count

s = input()
t = input()
ans = 9999999999
for i in range(len(s)-len(t)+1):
    ans = min(ans, check(t, s[i:i+len(t)]))
print(ans)