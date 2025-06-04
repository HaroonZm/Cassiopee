from sys import stdin

def main():
    it = iter(stdin)
    n = int(next(it).strip())
    for _ in range(n):
        cx = cy = maxValue = mx = my = 0
        while True:
            dx, dy = map(int, next(it).split())
            if dx == dy == 0:
                break
            cx += dx
            cy += dy
            d = cx * cx + cy * cy
            if (d > maxValue) or (d == maxValue and cx > mx):
                maxValue, mx, my = d, cx, cy
        print(f"{mx} {my}")

if __name__ == "__main__":
    main()