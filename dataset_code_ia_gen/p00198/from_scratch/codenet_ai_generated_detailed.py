# 解説
# 立方体は6面あるので、それぞれの面に色が割り当てられている。6色は固定で、順序は c1からc6。
# 立方体の向きを変える（回転させる）ことで、同じ色の配置でも異なる見え方がある。
# 我々は回転を考慮して、実質的に同じ配置になっている立方体を区別する必要がある。
# つまり、入力された各立方体の色配列について、その回転のすべてのパターンを考え、回転による等価クラスを求める。
# 同じ回転グループの中で最小の辞書順のパターンを代表として保持し、異なる代表パターンの個数を数える。
# 出展には6色すべて使われているので特別な判定は不要。

# 立方体の6面、入力の順序は問題文に明示されていないが、見本から推測すると
# c1 ~ c6順は、
# c1: 上面 (U)
# c2: 前面 (F)
# c3: 右面 (R)
# c4: 左面 (L)
# c5: 後面 (B)
# c6: 底面 (D)
# これを回転変換に使う。

# 立方体の回転を生成するには基本的に24通りある。

# アプローチ：
# 1. 各立方体の配列を読み込む。
# 2. 24回転を定義し、それぞれの回転で面の色の並びを生成。
# 3. 24回転で得られる配列の辞書順の最小を代表配列とする。
# 4. すべての立方体に対してこの代表配列を求め、集合に入れる。
# 5. 入力の個数 n と代表配列の個数 m を使い、n - m を出力（不足点数）。
# 6. データセットを繰り返し処理し、0が来たら終了。

# 以下にそのコードを示す。

def main():
    import sys

    input = sys.stdin.readline

    # 面の順序: U, F, R, L, B, D
    # 入力は c1 c2 c3 c4 c5 c6 の順
    # 回転パターンを定義する。24通り。

    # 回転定義のためのヘルパー関数
    # ここでは、回転後の面の位置を示すインデックス配列を作成する
    
    # 面の番号： 0:U, 1:F, 2:R, 3:L, 4:B, 5:D
    
    # 立方体の向きを変える基本回転は以下の3軸回転
    # 1) X軸回転: U→B→D→F→U (F->U, U->B, B->D, D->F)
    # 2) Y軸回転: F->R->B->L->F (F->R, R->B, B->L, L->F)
    # 3) Z軸回転: U->R->D->L->U (U->R, R->D, D->L, L->U)
    
    # 基本の回転をインデックスで記述し、それを組み合わせて24全ての回転行列を作成する
    
    # 各回転は面のインデックスの置き換え
    
    def rotate_x(face):
        # X軸回転
        # U->B, B->D, D->F, F->U を面番号に置き換える
        # R, Lは変わらず
        return [face[4], face[0], face[2], face[3], face[5], face[1]]

    def rotate_y(face):
        # Y軸回転
        # F->R, R->B, B->L, L->F
        # U, Dは変わらず
        return [face[0], face[3], face[1], face[4], face[2], face[5]]

    def rotate_z(face):
        # Z軸回転
        # U->R, R->D, D->L, L->U
        # F, Bは変わらず
        return [face[3], face[1], face[0], face[5], face[4], face[2]]

    # 回転24通りのすべてを生成

    def all_rotations(face):
        # faceは配列
        rotations = []
        # 基本的には6つのトップ面の選択と4つの回転(回転Z軸)の組み合わせ24通りを作成する方法
        # ここでは方式を変えて、24通り全探索する。

        # 立方体の24通りの向きは、以下の手順で生成可能

        # top面をUとするところに6通りある
        # 各topに対する周囲の回転は4通りなので6*4=24通り

        # まず、顔をfaceとして与えられた面配列を直接使う

        # topを0(U面),1(F面),2(R面),3(L面),4(B面),5(D面)として展開

        def rotate_to_top(face, top):
            tmp = face[:]
            # top面をU面に回す
            # topごとに回転をかける、以下は topをU面に持ってくる回転の逆

            # 顔の現在位置を [U,F,R,L,B,D]=[0,1,2,3,4,5] とする
            
            # top=0(U)のときは変化なし
            if top == 0:
                return tmp
            elif top == 1:  # F->U にするためX軸負方向回転
                # U->F -> X軸回転3回 (逆回転)
                for _ in range(3):
                    tmp = rotate_x(tmp)
                return tmp
            elif top == 2:  # R->U
                # U->R -> Z軸回転の逆回転3回
                for _ in range(3):
                    tmp = rotate_z(tmp)
                return tmp
            elif top == 3:  # L->U
                # U->L -> Z軸回転1回
                tmp = rotate_z(tmp)
                return tmp
            elif top == 4:  # B->U
                # U->B -> X軸回転1回
                tmp = rotate_x(tmp)
                return tmp
            elif top == 5:  # D->U
                # U->D -> X軸回転2回
                for _ in range(2):
                    tmp = rotate_x(tmp)
                return tmp

        results = []

        for top in range(6):
            base = rotate_to_top(face, top)
            # topをU面にしたので、Uは固定で、前面(1), 右面(2), 左面(3), 後面(4), 底面(5)が変わる
            # 周囲の4回転(前面周りのZ軸回転)を適用する
            tmp = base[:]
            for i in range(4):
                results.append(tmp)
                tmp = rotate_z(tmp)

        return results

    while True:
        n = input()
        if not n:
            break
        n = n.strip()
        if n == '0':
            break
        n = int(n)
        cubes = []
        for _ in range(n):
            colors = input().strip().split()
            cubes.append(colors)

        # 正規化集合を作る
        unique_reps = set()
        for cube in cubes:
            # 24回転を試して最小辞書順を探す
            rotations = all_rotations(cube)
            # rotationはリストのリスト
            # tupleにしてsetに入るように変換
            reps = []
            for r in rotations:
                reps.append(tuple(r))
            rep = min(reps)
            unique_reps.add(rep)

        # 出展に必要な点数 = n - 異なる立方体数
        print(n - len(unique_reps))

if __name__ == "__main__":
    main()