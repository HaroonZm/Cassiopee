H, W = map(int, input().split())
builds = []
for h in range(H):
    l = input()
    for w in range(W):
        if l[w] == "B":
            builds.append([h, w])
lu0 = H + W
lu1 = 0
ld0 = H + W
ld1 = 0
for pos in builds:
    h = pos[0]
    w = pos[1]
    hw = h + w
    hcw = H - h + w
    if hw < lu0:
        lu0 = hw
    if hw > lu1:
        lu1 = hw
    if hcw < ld0:
        ld0 = hcw
    if hcw > ld1:
        ld1 = hcw
diff1 = lu1 - lu0
diff2 = ld1 - ld0
if diff1 > diff2:
    print(diff1)
else:
    print(diff2)