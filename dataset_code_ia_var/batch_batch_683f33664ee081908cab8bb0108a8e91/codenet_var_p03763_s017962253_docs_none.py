n = int(input())
S = [input() for _ in range(n)]
l = [100] * 26
st = "abcdefghijklmnopqrstuvwxyz"
for i in S:
    for j in range(26):
        if l[j] > i.count(st[j]):
            l[j] = i.count(st[j])
ans = ""
for j in range(26):
    tmp = chr(97 + j) * l[j]
    ans += tmp
print(ans)