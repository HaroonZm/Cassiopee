N_K = input().split()
N = int(N_K[0])
K = int(N_K[1])
h = input().split()
for i in range(len(h)):
    h[i] = int(h[i])
cnt = 0
i = 0
while i < N:
    if h[i] >= K:
        cnt = cnt + 1
    i = i + 1
print(cnt)