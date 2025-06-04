n = int(input())
heights = [float(input()) for _ in range(n)]
bins = [0]*6
for h in heights:
    if h < 165.0:
        bins[0] += 1
    elif h < 170.0:
        bins[1] += 1
    elif h < 175.0:
        bins[2] += 1
    elif h < 180.0:
        bins[3] += 1
    elif h < 185.0:
        bins[4] += 1
    else:
        bins[5] += 1
for i, count in enumerate(bins, 1):
    print(f"{i}:" + "*"*count)