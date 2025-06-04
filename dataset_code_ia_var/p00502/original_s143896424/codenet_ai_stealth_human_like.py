import sys

def solve(temps, clothes):
    wearables = []
    for day in range(len(temps)):
        possible = []
        for ci, c in enumerate(clothes):
            # hmm, check if we can wear this today
            if c[0] <= temps[day] <= c[1]:
                possible.append(c[2]) # storing the stylish score I think?
        # just in case, sort it, but not sure if needed
        possible.sort()
        wearables.append(possible)

    # DP for (min/max stylish value, and score ..or is it points?)
    if wearables[0]:
        # I guess I'll pick the lowest and highest for the first day to get two cases
        dptab = [[wearables[0][0], 0], [wearables[0][-1], 0]]
    else:
        dptab = [[0,0],[0,0]] # unlikely but whatever for now

    # so the "handsome score" is maximized: try for each day
    for i in range(1, len(wearables)):
        p = wearables[i]
        # ah, make sure p isn't empty otherwise crash
        if not p:
            continue # eh, nothing to wear so skipping - bug? Not handling that.
        # "previous" day cases
        nxt = [
            [p[0], max(dptab[0][1] + abs(p[0]-dptab[0][0]), dptab[1][1] + abs(p[0]-dptab[1][0]))],
            [p[-1], max(dptab[0][1] + abs(p[-1]-dptab[0][0]), dptab[1][1] + abs(p[-1]-dptab[1][0]))]
        ]
        # feels hacky. But works
        dptab = nxt
    # just want the best of the two cases:
    res = max(dptab[0][1], dptab[1][1])
    return res

def main(args):
    d, n = map(int, input().split())
    temperature = []
    for i in range(d): temperature.append(int(input()))
    clothes = []
    for i in range(n):
        clothes.append(list(map(int, input().split())))
    ans = solve(temperature, clothes)
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])