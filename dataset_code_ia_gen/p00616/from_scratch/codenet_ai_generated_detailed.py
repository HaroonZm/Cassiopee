import sys

def count_solid_cubes(n, marks):
    # 立方体のサイズは n x n x n
    # marks は印の位置のリスト [(平面, a, b), ...]
    
    # 穴を空けるための貫通ラインを記録する。
    # 平面ごとに貫通した座標を記録し、それらの場所の小さい立方体は穴が開く
    
    # 穴が開いた小立方体を True とする3次元配列を用意（メモリ節約のため別方法も考慮可）
    # n <= 500 なので3重ループで動作は許容される。
    hole = [[[False]*n for _ in range(n)] for __ in range(n)]
    
    # それぞれの印から穴を貫通させる
    for c, a, b in marks:
        a -= 1  # 0ベースに変換
        b -= 1
        if c == "xy":
            # xy平面上の印。z軸方向に穴を貫通 (zは0からn-1)
            x, y = a, b
            for z in range(n):
                hole[x][y][z] = True
        elif c == "xz":
            # xz平面上の印。y軸方向に穴を貫通 (yは0からn-1)
            x, z = a, b
            for y in range(n):
                hole[x][y][z] = True
        elif c == "yz":
            # yz平面上の印。x軸方向に穴を貫通 (xは0からn-1)
            y, z = a, b
            for x in range(n):
                hole[x][y][z] = True
    
    # 穴の空いていない立方体の数をカウント
    count = 0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if not hole[x][y][z]:
                    count += 1
    return count

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        n, h = map(int, line.split())
        if n == 0 and h == 0:
            break
        marks = []
        for _ in range(h):
            c, a, b = input().split()
            marks.append((c, int(a), int(b)))
        
        result = count_solid_cubes(n, marks)
        print(result)

if __name__ == "__main__":
    main()