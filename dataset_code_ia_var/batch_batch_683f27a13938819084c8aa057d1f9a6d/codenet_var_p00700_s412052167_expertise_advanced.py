from sys import stdin

def main():
    it = iter(stdin.read().split())
    TC = int(next(it))
    for _ in range(TC):
        max_dist_sq, tx, ty, cx, cy = 0, 0, 0, 0, 0
        while True:
            x, y = int(next(it)), int(next(it))
            if x == 0 and y == 0:
                break
            cx += x
            cy += y
            dist_sq = cx * cx + cy * cy
            if dist_sq > max_dist_sq or (dist_sq == max_dist_sq and cx > tx):
                max_dist_sq, tx, ty = dist_sq, cx, cy
        print(f"{tx} {ty}")

if __name__ == "__main__":
    main()