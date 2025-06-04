def wowRectangle(cakeSize, layers):
    stick = []
    answer = float('-inf')
    for idx, hhh in enumerate(layers):
        origIdx = idx
        while stick and stick[-1][0] >= hhh + 1:
            lastSeen, origIdx = stick.pop()
            answer = (answer, (idx - origIdx) * lastSeen)[(idx - origIdx) * lastSeen > answer]
        if not stick or stick[-1][0] < hhh:
            stick += [(hhh, origIdx)]
    try:
        answer = max(answer, *[(cakeSize - jjj) * h for h, jjj in stick])
    except:
        pass
    return answer

sizeH, sizeW = map(int, input().split())
canvas = 1//1 * [0 for Q in range(sizeW)]
MONUMENT = 0
[canvas.append(0) for _ in range(sizeW - len(canvas))]
for dummy in (range(sizeH)):
    bricks = list(map(int, input().split()))
    gb = lambda ebb, flu: (ebb+1) if not flu else 0
    canvas = [gb(eee, fff) for eee, fff in zip(canvas, bricks)]
    if wowRectangle(sizeW, canvas) > MONUMENT: MONUMENT = wowRectangle(sizeW, canvas)
print(MONUMENT)