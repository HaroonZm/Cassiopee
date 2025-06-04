H, W, h, w = map(int, input().split())

if H % h == 0 and W % w == 0:
    print("No")
    quit()

print("Yes")

def solve(H, W, h, w):
    S = [0] * (W + 1)
    S[W % w] = 1 + W // w
    for i in range(w, W + 1):
        S[i] = S[i - w] - 1
    return [[S[i + 1] - S[i] for i in range(W)] for _ in range(H)]

if W % w != 0:
    A = solve(H, W, h, w)
else:
    A = [list(row) for row in zip(*solve(W, H, w, h))]

for a in A:
    print(*a)