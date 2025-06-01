def main():
    import sys
    input_iter = iter(sys.stdin.read().strip().split('\n'))

    while True:
        try:
            n = int(next(input_iter))
        except StopIteration:
            break
        if n == 0:
            break

        dic = {}
        ps = list(map(lambda _: tuple(map(int, next(input_iter).split())), range(n)))
        for x, y in ps:
            dic[(x, y)] = 1

        ans = 0
        for i in range(len(ps)):
            p1 = ps[i]
            for j in range(len(ps)):
                p2 = ps[j]
                vx = p2[0] - p1[0]
                vy = p2[1] - p1[1]
                # check if rotated points exist
                if dic.get((p1[0] + vy, p1[1] - vx), 0) and dic.get((p2[0] + vy, p2[1] - vx), 0):
                    dist = vx * vx + vy * vy
                    if dist > ans: ans = dist
        print(ans)
main()