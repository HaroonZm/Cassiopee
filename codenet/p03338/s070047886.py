n = int(input())
s = list(input())

cnt = 0
for i in range(n+2):
    c = set(s[0:i]) & set(s[i:n+1])
    if len(c) >= cnt:
        cnt = len(c)
print(cnt)