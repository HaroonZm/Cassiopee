def main():
    while True:
        N = int(input())
        if N == 0:
            break
        gems = set()
        for _ in range(N):
            x, y = map(int, input().split())
            gems.add((x, y))
        M = int(input())
        x, y = 10, 10
        collected = set()
        direction_map = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        # Check initial position if there's a gem
        if (x, y) in gems:
            collected.add((x, y))
        for _ in range(M):
            d, l = input().split()
            l = int(l)
            dx, dy = direction_map[d]
            for _ in range(l):
                x += dx
                y += dy
                if (x, y) in gems:
                    collected.add((x, y))
        print("Yes" if collected == gems else "No")

if __name__ == "__main__":
    main()