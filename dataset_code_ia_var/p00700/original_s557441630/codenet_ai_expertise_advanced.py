from sys import stdin

def main():
    n = int(input())
    lines = iter(stdin.readlines())
    for _ in range(n):
        from itertools import count
        cx, cy = maxx, maxy = maxL = 0
        for _ in count():
            dx_dy = next(lines).strip()
            dx, dy = map(int, dx_dy.split())
            if not (dx or dy):
                break
            cx, cy = cx + dx, cy + dy
            d = cx * cx + cy * cy
            if d > maxL or (d == maxL and cx > maxx):
                maxL, maxx, maxy = d, cx, cy
        print(f"{maxx} {maxy}")

if __name__ == '__main__':
    main()