lr = [0 for i in range(8)]
while True:
    try:
        a, b = map(float, input().split())
    except:
        break
    if a >= 1.1:
        lr[0] += 1
    elif a >= 0.6:
        lr[2] += 1
    elif a >= 0.2:
        lr[4] += 1
    else:
        lr[6] += 1
    if b >= 1.1:
        lr[1] += 1
    elif b >= 0.6:
        lr[3] += 1
    elif b >= 0.2:
        lr[5] += 1
    else:
        lr[7] += 1
print(lr[0], lr[1])
print(lr[2], lr[3])
print(lr[4], lr[5])
print(lr[6], lr[7])