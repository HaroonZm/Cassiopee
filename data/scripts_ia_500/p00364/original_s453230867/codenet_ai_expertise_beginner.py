N_t = input().split()
N = int(N_t[0])
t = int(N_t[1])

ts = []
for i in range(N):
    line = input().split()
    x = int(line[0])
    h = int(line[1])
    ts.append([x, h])

result = 0
for i in range(N):
    x = ts[i][0]
    h = ts[i][1]
    r = h * t / x
    if r > result:
        result = r

print(result)