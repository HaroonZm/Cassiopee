N = int(input())
Ls = list(map(int, input().split()))
Ls.sort()
i = 0
s = 0
while i < N:
    s += Ls[i]
    i += 2
print(s)