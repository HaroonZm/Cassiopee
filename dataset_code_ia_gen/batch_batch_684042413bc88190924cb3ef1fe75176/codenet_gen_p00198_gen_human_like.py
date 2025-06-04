def rotate(cube):
    # 回転による6方向の面の変化を返す関数
    # cubeは(c1,c2,c3,c4,c5,c6)の順で色が入っている
    # 回転しやすいように面のラベルを以下のように対応付ける
    # c1: 前(front), c2: 上(up), c3: 右(right), c4: 左(left), c5: 後(back), c6: 下(down)
    # 立方体の90度の回転を定義：前面を上に向けることや縦回転などの操作で全20通り（6面×4方向）を生成可能

    # 前方向を上にする回転（前→上、他も対応）
    def roll_x(c):
        # x軸回転 (front->up, up->back, back->down, down->front)
        return (c[1], c[4], c[2], c[3], c[5], c[0])

    def roll_y(c):
        # y軸回転 (front->right, right->back, back->left, left->front)
        return (c[3], c[1], c[0], c[5], c[4], c[2])

    def roll_z(c):
        # z軸回転 (up->right, right->down, down->left, left->up)
        return (c[0], c[3], c[1], c[5], c[2], c[4])

    # 与えられた立方体を20通りの姿勢に変換
    rotations = []
    c = tuple(cube)
    for i in range(6):
        if i == 1:
            c = roll_x(c)
        elif i == 2:
            c = roll_x(roll_x(c))
        elif i == 3:
            c = roll_x(roll_x(roll_x(c)))
        elif i == 4:
            c = roll_y(roll_x(c))
        elif i == 5:
            c = roll_y(roll_y(roll_y(c)))
        # ここで4回のz回転も行う
        temp = c
        for _ in range(4):
            rotations.append(temp)
            temp = roll_z(temp)
    return rotations

def normalize(cube):
    # cubeの20通りの回転から辞書順最小のパターンを返す
    return min(rotate(cube))

def main():
    while True:
        n = input().strip()
        if n == "0":
            break
        n = int(n)
        cubes = []
        for _ in range(n):
            line = input().strip().split()
            cubes.append(tuple(line))
        seen = set()
        duplicates = 0
        for cube in cubes:
            norm = normalize(cube)
            if norm in seen:
                duplicates += 1
            else:
                seen.add(norm)
        print(duplicates)

if __name__ == "__main__":
    main()