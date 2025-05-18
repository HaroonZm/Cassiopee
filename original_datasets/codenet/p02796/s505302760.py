def main():
    n = int(input())
    robots = []
    for _ in range(n):
        x, l = map(int, input().split())
        robots.append((x-l, x+l))
    robots.sort(key=lambda x: x[1])
    count = 1
    robot = robots[0]
    for r in robots:
        if robot[1] <= r[0]:
            robot = r
            count += 1
    print(count)

if __name__ == "__main__":
    main()