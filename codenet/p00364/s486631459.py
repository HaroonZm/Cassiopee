N,t = [int(i) for i in input().split()]

r = 0.0

for l in range(N):
    x,h = [float(i) for i in input().split()]
    r = max(r, h / x)

print(float(t)*r)