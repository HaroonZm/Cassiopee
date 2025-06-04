N_K = input().split()
N = int(N_K[0])
K = int(N_K[1])

def next_mult(val, step):
    return val * step

cnt = 1
tmp = K
for _ in range(1000):
    if tmp > N:
        break
    tmp = next_mult(tmp, K)
    cnt = cnt + 1
print(cnt)