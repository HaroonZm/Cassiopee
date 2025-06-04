while True:
    n = int(input())
    if n == 0:
        break
    chars = []
    times = {}
    for _ in range(n):
        data = input().split()
        name = data[0]
        m = int(data[1])
        tlist = list(map(int, data[2:2+m]))
        chars.append(name)
        for t in tlist:
            if t not in times:
                times[t] = []
            times[t].append(name)
    points = {c:0 for c in chars}
    for t in times:
        l = len(times[t])
        for c in times[t]:
            points[c] += l
    min_point = min(points.values())
    min_chars = [c for c,v in points.items() if v == min_point]
    print(min_point, sorted(min_chars)[0])