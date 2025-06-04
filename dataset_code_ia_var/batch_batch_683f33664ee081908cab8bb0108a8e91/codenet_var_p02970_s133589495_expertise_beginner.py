N_D = input().split(' ')
N = int(N_D[0])
D = int(N_D[1])

d = 2 * D + 1
cnt = 1

while N > d:
    cnt = cnt + 1
    d = d + (2 * D + 1)

print(cnt)