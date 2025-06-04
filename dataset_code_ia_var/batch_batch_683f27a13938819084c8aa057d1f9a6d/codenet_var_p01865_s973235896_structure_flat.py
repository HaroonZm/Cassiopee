l = int(input())
n = int(input())
mom = 0
i = 0
while i < n:
    xw = input().split()
    x = int(xw[0])
    w = int(xw[1])
    mom += x * w
    i += 1
weight = []
while mom != 0:
    if mom < 0:
        add_weight = -mom
        if add_weight > 50000:
            add_weight = 50000
        mom += add_weight
        weight.append((1, add_weight))
    elif mom > 0:
        add_weight = mom
        if add_weight > 50000:
            add_weight = 50000
        mom -= add_weight
        weight.append((-1, add_weight))
print(len(weight))
i = 0
while i < len(weight):
    t = weight[i]
    print(t[0], t[1])
    i += 1