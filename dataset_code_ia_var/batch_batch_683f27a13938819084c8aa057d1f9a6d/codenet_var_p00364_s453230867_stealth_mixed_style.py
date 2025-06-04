from functools import reduce

N_t = input().split()
N = int(N_t[0])
t = int(N_t[1])

ts = []
for i in range(N):
    tmp = list(map(int, input().split()))
    ts.append(tmp)

def calc(mx, curr):
    return mx if mx > curr else curr

res = 0
idx = 0
while idx < len(ts):
    a, b = ts[idx]
    r = float(b) * t / a
    res = calc(res, r)
    idx += 1

print(res)