s = input()
k = int(input())
s = list(s)
n = len(s)

for i in range(n):
    pos = i
    for j in range(i + 1, min(n, i + k + 1)):
        if s[j] < s[pos]:
            pos = j
    for j in range(pos, i, -1):
        s[j], s[j - 1] = s[j - 1], s[j]
    k -= (pos - i)
    if k <= 0:
        break

print("".join(s))