import sys

def main():
    input = sys.stdin.readline

    while True:
        n, h = map(int, input().split())
        if n == 0 and h == 0:
            break

        # 初期状態: 穴が空いていない小立方体をTrueで管理する3D配列
        # メモリ節約のためnが最大500なので、bool型の配列をリスト内包表現で作成
        cube = [[[True] * n for _ in range(n)] for __ in range(n)]

        # 穴が開く立方体を管理する3つの方向別の配列を用意
        # xy面の印ならz方向に穴が貫通
        # xz面の印ならy方向に穴が貫通
        # yz面の印ならx方向に穴が貫通

        # 穴があく処理を行う関数を定義
        def drill_hole(plane, a, b):
            if plane == 'xy':
                # xy平面の穴はz方向に貫通、x=a, y=b固定
                x = a - 1
                y = b - 1
                for z in range(n):
                    cube[z][y][x] = False
            elif plane == 'xz':
                # xz平面の穴はy方向に貫通、x=a, z=b固定
                x = a - 1
                z = b - 1
                for y in range(n):
                    cube[z][y][x] = False
            else:
                # yz平面の穴はx方向に貫通、y=a, z=b固定
                y = a - 1
                z = b - 1
                for x in range(n):
                    cube[z][y][x] = False

        for _ in range(h):
            c, a, b = input().split()
            a = int(a)
            b = int(b)
            drill_hole(c, a, b)

        # 穴の空いていない小立方体の個数を数える
        count = 0
        for z in range(n):
            for y in range(n):
                for x in range(n):
                    if cube[z][y][x]:
                        count += 1

        print(count)

if __name__ == '__main__':
    main()