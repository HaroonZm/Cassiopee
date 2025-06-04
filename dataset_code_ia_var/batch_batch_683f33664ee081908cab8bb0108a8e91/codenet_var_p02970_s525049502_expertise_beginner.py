N_D = input().split()
N = int(N_D[0])
D = int(N_D[1])

a = 0
while N > 0:
    N = N - (2 * D + 1)
    a = a + 1

print(a)