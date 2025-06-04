n = int(input())
heights = []
for i in range(n):
    h = float(input())
    heights.append(h)

counts = [0, 0, 0, 0, 0, 0]

for h in heights:
    if h < 165.0:
        counts[0] += 1
    elif h < 170.0:
        counts[1] += 1
    elif h < 175.0:
        counts[2] += 1
    elif h < 180.0:
        counts[3] += 1
    elif h < 185.0:
        counts[4] += 1
    else:
        counts[5] += 1

for i in range(6):
    print(str(i+1) + ":" + "*" * counts[i])