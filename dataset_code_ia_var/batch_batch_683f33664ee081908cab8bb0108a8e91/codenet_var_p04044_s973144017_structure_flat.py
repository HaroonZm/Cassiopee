N_L = input().split()
N = int(N_L[0])
L = int(N_L[1])
s = []
i = 0
while i < N:
    s.append(input())
    i += 1
s.sort()
ans = ''
j = 0
while j < len(s):
    ans += s[j]
    j += 1
print(ans)