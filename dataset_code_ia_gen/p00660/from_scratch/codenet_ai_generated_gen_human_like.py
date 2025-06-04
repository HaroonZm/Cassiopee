import sys

# 定数：数字の7x7パターン
digit_patterns = {
    1: [
        "#######",
        "#.....#",
        "#...|.#",
        "#.....#",
        "#...|.#",
        "#..-..#",
        "#######",
    ],
    2: [
        "#######",
        "#..-..#",
        "#...|.#",
        "#..-..#",
        "#.|...#",
        "#..-..#",
        "#######",
    ],
    3: [
        "#######",
        "#..-..#",
        "#...|.#",
        "#..-..#",
        "#...|.#",
        "#..-..#",
        "#######",
    ],
    4: [
        "#######",
        "#.....#",
        "#.|.|.#",
        "#..-..#",
        "#...|.#",
        "#.....#",
        "#######",
    ],
    5: [
        "#######",
        "#..-..#",
        "#.|...#",
        "#..-..#",
        "#...|.#",
        "#..-..#",
        "#######",
    ],
    6: [
        "#######",
        "#..-..#",
        "#.|...#",
        "#..-..#",
        "#.|.|.#",
        "#..-..#",
        "#######",
    ],
    7: [
        "#######",
        "#..-..#",
        "#...|.#",
        "#.....#",
        "#...|.#",
        "#.....#",
        "#######",
    ],
    8: [
        "#######",
        "#..-..#",
        "#.|.|.#",
        "#..-..#",
        "#.|.|.#",
        "#..-..#",
        "#######",
    ],
    9: [
        "#######",
        "#..-..#",
        "#.|.|.#",
        "#..-..#",
        "#...|.#",
        "#..-..#",
        "#######",
    ],
}

# 入力される数字： '|','-'の変換や回転を考慮して一致判定
def rotate_grid_90(grid):
    h = len(grid)
    w = len(grid[0])
    new_grid = []
    for c in range(w):
        row = []
        for r in range(h-1, -1, -1):
            # 90度回転で '|' と '-' を入れ替え
            ch = grid[r][c]
            if ch == '|':
                ch = '-'
            elif ch == '-':
                ch = '|'
            row.append(ch)
        new_grid.append(''.join(row))
    return new_grid

def rotate_grid_270(grid):
    # 270度回転は90度回転3回と同義
    return rotate_grid_90(rotate_grid_90(rotate_grid_90(grid)))

def flip_horizontal(grid):
    return [line[::-1] for line in grid]

def flip_vertical(grid):
    return grid[::-1]

# 与えられた7x7グリッドが数字何か判定
def identify_digit(grid):
    # 元の数字のパターン列挙
    base_patterns = []
    for digit, pat in digit_patterns.items():
        base_patterns.append( (digit, pat) )
    # 回転や反転して比較
    for digit, base in base_patterns:
        # baseは元の7x7
        # 与えられたgridは数字表示の変換済み？
        # candidate は base を 反転または回転したもので一致を探す
        # 反転自体が入力に元々入っているので基本形(base)から変換種類を試す
        for trans in generate_transformations(base):
            if grids_equal(trans, grid):
                return digit
    # なければNone（ありえないはず）
    return None

def grids_equal(g1, g2):
    if len(g1) != len(g2):
        return False
    for r in range(len(g1)):
        if g1[r] != g2[r]:
            return False
    return True

def generate_transformations(grid):
    # gridを元に可能な変換を返すジェネレータ
    # 入力の数字は「左右反転」や「左右反転のあと反時計回り90度回転」など計6種類があるので
    # それらを元の数字パターンに対して試せば解決する
    
    # 変換手順は以下6つ（問題文）
    # 1. 左右反転
    # 2. 左右反転 + 反時計回り90度回転
    # 3. 左右反転
    # 4. 左右反転 + 反時計回り270度回転
    # 5. 左右反転
    # 6. 上下反転 + 左右反転
    
    # ただし5は1と同じなので冗長？
    # 実際には6種類は以下
    # 左右反転
    # 左右反転 + CCW90
    # 左右反転 + CCW270
    # 上下反転 + 左右反転
    # 左右反転 (同じなので省略)
    # 左右反転 + CCW270 (同じ１つの繰り返し？)
    # -> 実質4種類変換
    
    fh = flip_horizontal(grid)
    yield fh
    yield rotate_grid_90(fh)
    yield rotate_grid_270(fh)
    fv = flip_vertical(grid)
    yield flip_horizontal(fv)

def extract_subgrid(grid, r0, c0, h=7, w=7):
    return [grid[r0+i][c0:c0+w] for i in range(h)]

# サイコロの目の左上座標
player_faces_pos = [(0,7),(7,0),(7,7),(7,14),(7,21),(14,7)]
dealer_faces_pos = [(0,36),(7,29),(7,36),(7,43),(7,50),(14,36)]

def read_dice_faces(grid, face_pos):
    faces = []
    for (r,c) in face_pos:
        sub = extract_subgrid(grid, r, c)
        digit = identify_digit(sub)
        faces.append(digit)
    return faces

def main():
    lines = []
    for line in sys.stdin:
        line = line.rstrip('\n')
        if line == '0':
            break
        lines.append(line)
        if len(lines) == 21:
            # linesに21行ある => 1ケースの入力読了
            
            # 参加者グリッド0..20行、0..27列
            player_grid = [l[:28] for l in lines]
            # おじさんグリッド0..20行、29..56列
            dealer_grid = [l[29:57] for l in lines]
            
            player_faces = read_dice_faces(player_grid, player_faces_pos)
            dealer_faces = read_dice_faces(dealer_grid, dealer_faces_pos)
            
            # 点数の組み合わせ計算
            # 各面は一様分布と仮定してそれぞれ1/6
            # 同じ目は再投 -> 除外
            
            # 確率計算
            win_high = 0.0
            win_low = 0.0
            total_prob = 0.0
            for p_face in player_faces:
                for d_face in dealer_faces:
                    if p_face == d_face:
                        continue
                    total_prob += 1.0
                    if p_face > d_face:
                        win_high += 1.0
                    else:
                        win_low += 1.0
            
            # probability normalize
            if total_prob == 0:
                # 引き分けのみで終わるダイスは与えられない問題文より
                # 起こらないが安全のためHIGH出す
                print("HIGH")
            else:
                ph = win_high / total_prob
                pl = win_low / total_prob
                if ph >= pl:
                    print("HIGH")
                else:
                    print("LOW")
            
            lines = []

if __name__ == '__main__':
    main()