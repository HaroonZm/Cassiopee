n = int(input())
heights = []
for i in range(n):
    h = float(input())
    heights.append(h)

count = [0, 0, 0, 0, 0, 0]

for h in heights:
    if h < 165.0:
        count[0] += 1
    elif h < 170.0:
        count[1] += 1
    elif h < 175.0:
        count[2] += 1
    elif h < 180.0:
        count[3] += 1
    elif h < 185.0:
        count[4] += 1
    else:
        count[5] += 1

for i in range(6):
    print(str(i+1) + ":" + "*" * count[i])