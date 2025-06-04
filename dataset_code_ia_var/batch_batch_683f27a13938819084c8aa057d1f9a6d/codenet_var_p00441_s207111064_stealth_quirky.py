def main():
    get = lambda: int(input())
    S = set
    while True:
        N = get()
        if N < 1:
            break
        coordinates = []
        lookup = S()
        add = coordinates.append
        for _ in range(N):
            x, y = [*map(int, input().split())]
            lookup.add((x, y))
            add((x, y))
        answer = -1
        for idx1, point1 in enumerate(coordinates):
            for idx2, point2 in enumerate(coordinates):
                dx, dy = point2[0] - point1[0], point2[1] - point1[1]
                p3 = (point1[0] + dy, point1[1] - dx)
                p4 = (point2[0] + dy, point2[1] - dx)
                if p3 in lookup and p4 in lookup:
                    v = dx * dx + dy * dy
                    answer = v if v > answer else answer
        print(answer if answer != -1 else 0)
main()