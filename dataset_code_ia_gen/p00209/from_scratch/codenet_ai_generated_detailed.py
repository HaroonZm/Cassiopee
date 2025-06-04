import sys
sys.setrecursionlimit(10**7)

# 回転関数：切れ端の2次元リストを90度反時計回りに回転させる
def rotate_90(mat):
    m = len(mat)
    rotated = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rotated[m-j-1][i] = mat[i][j]
    return rotated

# 指定された座標が接続の範囲内か判定
def in_bounds(x, y, m):
    return 0 <= x < m and 0 <= y < m

# 切れ端の連結成分を探索するDFS
def dfs_patch(patch, visited, x, y):
    stack = [(x,y)]
    visited[x][y] = True
    coords = [(x,y)]
    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = cx + dx, cy + dy
            if in_bounds(nx, ny, len(patch)) and not visited[nx][ny] and patch[nx][ny] >= 0:
                visited[nx][ny] = True
                stack.append((nx, ny))
                coords.append((nx, ny))
    return coords

# 切れ端のどのマスが画像データを持っているかのマスクを返す
def make_mask(patch):
    m = len(patch)
    mask = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if patch[i][j] >= 0:
                mask[i][j] = 1
    return mask

# 画像部分の連結検査。穴あきもあり得るが、必ず1成分のみ。頂点だけ接しているのは不可。
# maskは0か1の値である必要あり
def is_connected(mask):
    m = len(mask)
    visited = [[False]*m for _ in range(m)]
    # 画像部分のマス数カウント
    count = sum(sum(row) for row in mask)
    if count == 0:
        return False
    # どれか１つマスを探してDFSスタート
    for i in range(m):
        for j in range(m):
            if mask[i][j] == 1:
                coords = dfs_patch(mask, visited, i, j)
                # DFSで訪問したマスと画像マスの数が一致すれば連結
                if len(coords) == count:
                    return True
                else:
                    return False
    return False

# 窓の外の景色wの中に、写真patchを各回転ごとに照合
def match(w, patch):
    n = len(w)
    m = len(patch)
    # patchの画像部分位置
    coords = []
    for i in range(m):
        for j in range(m):
            if patch[i][j] >= 0:
                coords.append((i,j))

    # 照合用
    candidates = []
    # 窓の中で、切れ端を置ける範囲の全探索
    for x in range(n - m + 1):
        for y in range(n - m + 1):
            matched = True
            for i, j in coords:
                # w の (x+i,y+j) と patch の(i,j)が同じか？
                if w[x+i][y+j] != patch[i][j]:
                    matched = False
                    break
            if matched:
                candidates.append((x,y))
    return candidates

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        n_m = line.strip().split()
        if len(n_m) < 2:
            continue
        n, m = map(int, n_m)
        if n == 0 and m == 0:
            break
        # 景色の読み込み
        w = [list(map(int,input().split())) for _ in range(n)]
        # 切れ端の読み込み
        patch = [list(map(int,input().split())) for _ in range(m)]

        # 切れ端の画像部分の連結確認
        mask = make_mask(patch)
        if not is_connected(mask):
            # 条件より連結していることが前提だが念のため処理続行
            print("NA")
            continue

        # 回転パターンの作成
        patches = []
        cur = patch
        for _ in range(4):
            patches.append(cur)
            cur = rotate_90(cur)

        # 見つかった領域の候補(座標)一覧を集める
        all_candidates = []
        for p in patches:
            cands = match(w, p)
            if cands:
                all_candidates.extend(cands)

        if not all_candidates:
            print("NA")
        else:
            # 最も上端に近い（xが最小）→その中で最も左端に近い（yが最小）
            all_candidates.sort()
            x_ans, y_ans = all_candidates[0]
            # 1-indexedが問題文中指定なしだが入力例出力例より1-basedと思われる
            print(x_ans+1, y_ans+1)

if __name__ == "__main__":
    main()