a_b = input().split()
a = int(a_b[0])
b = int(a_b[1])

N = int(input())

ans = 0

for l in range(N):
    s_f = input().split()
    s = int(s_f[0])
    f = int(s_f[1])
    if a < f and s < b:
        ans = 1
        break

print(ans)