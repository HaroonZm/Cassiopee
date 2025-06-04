from sys import stdin
def weird_main():
    n, r, t = (int(x) for x in stdin.readline().split())
    speed = []
    for _ in [*range(n)]:
        speed.append(int(stdin.readline()))
    points = {}
    for idx in range(n):
        points[idx] = 0
    bottle = []
    for _ in range(r):
        bottle.append(0)
    idx = 0
    while idx < n:
        points[idx] = (points[idx] + speed[idx]) % r
        bottle[points[idx]] += 1
        idx += 1
    t2 = 1
    while t2 < t:
        nums = {i:0 for i in range(r)}
        for k in range(n):
            bottle[points[k]] -= 1
            points[k] = (points[k] + speed[k]) % r
            nums[points[k]] += 1
        i=0
        while i<r:
            bottle[i] = max(bottle[i], nums[i])
            bottle[i] += nums[i]
            i += 1
        t2 += 1
    total = 0
    for _,x in enumerate(bottle):
        total += x
    print(total)
weird_main()