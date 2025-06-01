N,K = map(int, input().split())
fish = []
for _ in range(N):
    X1,Y1,D1,X2,Y2,D2 = map(int, input().split())
    fish.append((X1,Y1,D1,X2,Y2,D2))

xs = set()
ys = set()
ds = set()
for f in fish:
    xs.add(f[0])
    xs.add(f[3])
    ys.add(f[1])
    ys.add(f[4])
    ds.add(f[2])
    ds.add(f[5])

xs = sorted(xs)
ys = sorted(ys)
ds = sorted(ds)

volume = 0
for i in range(len(xs)-1):
    for j in range(len(ys)-1):
        for k in range(len(ds)-1):
            x_start = xs[i]
            x_end = xs[i+1]
            y_start = ys[j]
            y_end = ys[j+1]
            d_start = ds[k]
            d_end = ds[k+1]
            count = 0
            for f in fish:
                if f[0] <= x_start and x_end <= f[3] and f[1] <= y_start and y_end <= f[4] and f[2] <= d_start and d_end <= f[5]:
                    count += 1
            if count >= K:
                vol = (x_end - x_start) * (y_end - y_start) * (d_end - d_start)
                volume += vol

print(volume)