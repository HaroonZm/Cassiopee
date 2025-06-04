from collections import deque

def main():
    N, M = map(int, input().split())
    grid = [list(input()) for _ in range(N)]

    # 方角と向きの対応
    # 上:0, 右:1, 下:2, 左:3
    dir_map = {'^':0, '>':1, 'v':2, '<':3}
    # 移動ベクトル
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 右手の位置は、向きによって決まる右方向
    # 右方向は (dir + 1) % 4
    # B君の位置と向きと右手の位置を記録する必要があるため右手の位置は座標で管理

    # 探すスタート位置・向き・右手位置を見つける
    start_x = start_y = start_dir = None
    goal_x = goal_y = None
    for i in range(N):
        for j in range(M):
            c = grid[i][j]
            if c in dir_map:
                start_x, start_y = i, j
                start_dir = dir_map[c]
            elif c == 'G':
                goal_x, goal_y = i, j

    # 右手の初期接触位置
    # 初期方向に対して右手は右側の壁に接している
    # つまり、start_x + dx[(start_dir+1)%4], start_y + dy[(start_dir+1)%4]
    right_x = start_x + dx[(start_dir+1)%4]
    right_y = start_y + dy[(start_dir+1)%4]

    # 右手は必ず壁に接している
    # 外壁は壁なので範囲外でなく壁であることは保証されているが念のため確認
    if not (0 <= right_x < N and 0 <= right_y < M and grid[right_x][right_y] == '#'):
        # 条件より初期状態は右手は壁に接しているはず
        print(-1)
        return

    # 右手が届く範囲：B君の向きに対して
    # 正面 (dir), 斜め右前 (dir+1,+-1), 右 (dir+1), 斜め右後ろ (dir+2,+-1)
    # 具体的には、4マスは以下のようになる
    # 正面: (x + dx[dir], y + dy[dir])
    # 斜め右前: (x + dx[dir] + dx[(dir+1)%4], y + dy[dir] + dy[(dir+1)%4])
    # 右: (x + dx[(dir+1)%4], y + dy[(dir+1)%4])
    # 斜め右後ろ: (x - dx[dir] + dx[(dir+1)%4], y - dy[dir] + dy[(dir+1)%4])

    # 右手が接している場所は上記4マスの中の1つである必要がある

    # 右手のタイル間切り替えは右手接触タイルの変更のことで、
    # 複数タイルからの変更時は変更前後のタイルが共通点を持っている必要がある
    # つまり、隣接または角でつながっている場所だけ遷移可能

    # BFS 状態: (x, y, dir, right_x, right_y)
    # 訪問済み記録: 四次元配列
    visited = [[[[False]*M for _ in range(N)] for _ in range(4)] for _ in range(N*M)]
    # 座標の管理を変え、4次元配列で visited[x][y][dir][right_x*M+right_y]
    # だが扱いづらいので辞書を使う

    visited_dict = set()
    def encode_state(x,y,d,r_x,r_y):
        return (x,y,d,r_x,r_y)

    # 距離（通った異なるマスの数の最小）管理、位置が変わった時だけインクリメント
    # 位置変更時にのみカウントアップ

    q = deque()
    start_state = (start_x, start_y, start_dir, right_x, right_y)
    q.append((start_state, 1)) # 位置開始カウントは1
    visited_dict.add(encode_state(*start_state))

    # 右手が届く位置リストを計算
    def right_hand_reach(x,y,d):
        lst = []
        d0 = d
        d1 = (d+1)%4
        # 正面
        lst.append((x+dx[d0], y+dy[d0]))
        # 斜め右前
        lst.append((x+dx[d0]+dx[d1], y+dy[d0]+dy[d1]))
        # 右
        lst.append((x+dx[d1], y+dy[d1]))
        # 斜め右後ろ
        lst.append((x - dx[d0] + dx[d1], y - dy[d0] + dy[d1]))
        return lst

    # 隣接(8方向)判定
    adj8 = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    def is_adjacent(a,b,c,d):
        return max(abs(a-c), abs(b-d)) == 1 or (a==c and b==d)

    while q:
        (x,y,d,r_x,r_y), dist = q.popleft()

        # ゴール判定
        if (x,y)==(goal_x, goal_y):
            print(dist)
            return

        # 右手が届く場所
        reachable = right_hand_reach(x,y,d)

        # 現在の右手装着位置がreachable内にあるかチェック
        # 必須条件：右手が届く範囲のうちの一つである
        if (r_x, r_y) not in reachable:
            continue

        # 1. 前方に壁がなければ1マス進む
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != '#':
            # 右手の接触箇所はそのまま (r_x, r_y) ではまずい
            # 移動すると右手が届く範囲も移動後のものになる → チェックと調整要

            # 移動後の右手が届く範囲
            next_reach = right_hand_reach(nx, ny, d)
            # 右手を離さずにいくには、
            # 移動前の右手接触箇所(r_x,r_y) と
            # 移動後の右手接触箇所もreachable範囲でなければならない

            if (r_x, r_y) in next_reach:
                new_state = (nx, ny, d, r_x, r_y)
                s_code = encode_state(*new_state)
                if s_code not in visited_dict:
                    visited_dict.add(s_code)
                    # 位置が変わったから通ったマス数は増加
                    q.append((new_state, dist + 1))
        # 2. 向きの変更(右90度)
        nd = (d + 1) % 4
        # 右手が届く範囲が変わるので、右手位置をnd方向での範囲内に調整しないといけない
        # 右手を離さないためには、変更前のマス(r_x,r_y)と変更後の右手のマスとの間が接している必要がある

        next_reach = right_hand_reach(x, y, nd)
        for nr_x, nr_y in next_reach:
            if 0 <= nr_x < N and 0 <= nr_y < M:
                # 壁である必要はない? 右手は壁に接触している必要がある
                if grid[nr_x][nr_y] == '#':
                    # 変更前の壁(r_x,r_y) と変更後壁(nr_x,nr_y)が隣接(共通点持つ)か確認
                    if is_adjacent(r_x,r_y,nr_x,nr_y):
                        new_state = (x, y, nd, nr_x, nr_y)
                        s_code = encode_state(*new_state)
                        if s_code not in visited_dict:
                            visited_dict.add(s_code)
                            # 向き変更なので位置は変わっていない → distは増加しない
                            q.append((new_state, dist))

        # 3. 向きの変更(左90度)
        nd = (d + 3) % 4  # 左回転
        next_reach = right_hand_reach(x, y, nd)
        for nr_x, nr_y in next_reach:
            if 0 <= nr_x < N and 0 <= nr_y < M:
                if grid[nr_x][nr_y] == '#':
                    if is_adjacent(r_x,r_y,nr_x,nr_y):
                        new_state = (x, y, nd, nr_x, nr_y)
                        s_code = encode_state(*new_state)
                        if s_code not in visited_dict:
                            visited_dict.add(s_code)
                            q.append((new_state, dist))

        # 4. 右手の位置変更
        # 右手が届く範囲内の壁で共通点のあるものに変更可能
        next_reach = right_hand_reach(x, y, d)
        for nr_x, nr_y in next_reach:
            if 0 <= nr_x < N and 0 <= nr_y < M:
                if grid[nr_x][nr_y] == '#':
                    if (nr_x,nr_y) != (r_x,r_y) and is_adjacent(r_x,r_y,nr_x,nr_y):
                        new_state = (x, y, d, nr_x, nr_y)
                        s_code = encode_state(*new_state)
                        if s_code not in visited_dict:
                            visited_dict.add(s_code)
                            # 位置は変わらないからdist変わらず
                            q.append((new_state, dist))

    # 到達不可能
    print(-1)

if __name__ == "__main__":
    main()