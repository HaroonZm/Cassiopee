import math

def main():
    while True:
        n = int(input())
        if n == -1:
            break

        # 初期状態：井戸から東に1mの地点に立つ
        x = 1.0
        y = 0.0
        # 井戸の方向は西向き（東の逆方向）
        dx = -1.0
        dy = 0.0

        for _ in range(n):
            # まっすぐ井戸の方向を向くので(dx, dy)は変わらず
            # 右回りに90度向きを変える → (dx, dy)を(0,1)→(1,0)→(0,-1)→(-1,0)のように回す
            # 右回り90度回転: (dx, dy) → (dy, -dx)
            ndx = dy
            ndy = -dx
            dx, dy = ndx, ndy

            # 1m直進
            x += dx
            y += dy

        print("{0:.2f}".format(x))
        print("{0:.2f}".format(y))

if __name__ == "__main__":
    main()