from sys import stdin
s = stdin.readline().rstrip()
k = "CODEFESTIVAL2016"
point = 0
for i in range(len(s)):
    if k[i] != s[i]:
        point += 1
print(point)