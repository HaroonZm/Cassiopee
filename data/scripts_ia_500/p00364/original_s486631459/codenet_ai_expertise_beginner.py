N, t = input().split()
N = int(N)
t = int(t)

r = 0.0

for i in range(N):
    line = input().split()
    x = float(line[0])
    h = float(line[1])
    value = h / x
    if value > r:
        r = value

result = t * r
print(result)