from sys import stdin

def main():
    it = iter(stdin.read().split())
    for _ in range(int(next(it))):
        ans_sq, xpos, ypos, best_x, best_y = 0, 0, 0, 0, 0
        while True:
            dx, dy = int(next(it)), int(next(it))
            if not (dx | dy):
                break
            xpos += dx
            ypos += dy
            dist_sq = xpos * xpos + ypos * ypos
            if dist_sq > ans_sq:
                ans_sq, best_x, best_y = dist_sq, xpos, ypos
            elif dist_sq == ans_sq and xpos > best_x:
                best_x, best_y = xpos, ypos
        print(f"{best_x} {best_y}")

if __name__ == "__main__":
    main()