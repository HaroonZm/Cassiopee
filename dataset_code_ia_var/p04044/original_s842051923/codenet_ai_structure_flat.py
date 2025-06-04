n_l = input().split()
n = int(n_l[0])
l = int(n_l[1])
i = 0
s = []
while i < n:
    s.append(input())
    i += 1
s.sort()
i = 0
while i < len(s):
    print(s[i], end="")
    i += 1