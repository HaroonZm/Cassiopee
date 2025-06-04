# 簡単なシミュレーションを行う初心者向けの実装例

def main():
    import sys

    # 幽霊の移動方向の対応
    move_map = {
        '5': (0,0),
        '8': (-1,0),
        '6': (0,1),
        '4': (0,-1),
        '2': (1,0),
    }

    for line in sys.stdin:
        if line.strip() == '':
            continue
        H,W = map(int,line.split())
        if H == 0 and W == 0:
            break
        grid = []
        girl_pos = None
        ghost_pos = None
        for i in range(H):
            row = list(sys.stdin.readline().rstrip('\n'))
            for j,c in enumerate(row):
                if c == 'A':
                    girl_pos = (i,j)
                    row[j] = '.'  # 移動可能マスとして扱う
                elif c == 'B':
                    ghost_pos = (i,j)
                    row[j] = '.'
            grid.append(row)
        pattern = sys.stdin.readline().rstrip('\n')
        L = len(pattern)

        # 移動できるか判定（少女用）
        def can_move_for_girl(r,c):
            if r < 0 or r >= H or c < 0 or c >= W:
                return False
            # 女の子は '.' のみ入れる（'#' は入れない）
            if grid[r][c] == '.':
                return True
            else:
                return False

        # 幽霊の移動可否（幽霊は '#' と '.' に入れる）
        def can_move_for_ghost(r,c):
            if r < 0 or r >= H or c < 0 or c >= W:
                return False
            if grid[r][c] == '.' or grid[r][c] == '#':
                return True
            else:
                return False

        # 幽霊の位置の時刻ごとの候補を求める（幽霊は行動パターンに従うので、状態は(位置,idx)で固定）
        from collections import deque

        max_time = 500   # 適当な大きさの上限を設定（最悪ここまで探索）

        # 幽霊の時刻毎の位置を記録。幽霊は行動パターンでループする。
        # ghost_states[t] = (r,c)
        ghost_states = []

        gr, gc = ghost_pos
        idx = 0
        ghost_states.append((gr,gc))
        for t in range(1, max_time+1):
            dr, dc = move_map[pattern[idx]]
            nr, nc = gr + dr, gc + dc
            if can_move_for_ghost(nr,nc):
                gr, gc = nr, nc
            # できなければ留まる（位置はそのまま）
            ghost_states.append((gr,gc))
            idx = (idx+1) % L

        # 女の子は自由に移動できるのでBFSで探索（状態は位置と時刻）
        # ただし時刻は最大探索時間まで
        from collections import deque
        visited = [[-1]*W for _ in range(H)]  # 最も早い到達時刻を記録
        visited_times = [[set() for _ in range(W)] for _ in range(H)]

        q = deque()
        q.append((girl_pos[0],girl_pos[1],0))
        visited_times[girl_pos[0]][girl_pos[1]].add(0)

        found = False
        ans_time = -1
        ans_r = -1
        ans_c = -1

        while q:
            r,c,t = q.popleft()
            if t > max_time:
                break

            # 幽霊の位置と同じなら遭遇
            if t < len(ghost_states):
                gr, gc = ghost_states[t]
                if r == gr and c == gc:
                    found = True
                    ans_time = t
                    ans_r = r
                    ans_c = c
                    break

            # 次の行動（5方向）
            for dr, dc in [(0,0),(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                # 移動可能か
                if 0 <= nr < H and 0 <= nc < W:
                    if grid[nr][nc] == '.':
                        nt = t+1
                        # 時刻毎に操作するので重複防止は時刻も含める
                        if nt not in visited_times[nr][nc]:
                            visited_times[nr][nc].add(nt)
                            q.append((nr,nc,nt))
                else:
                    # 範囲外は移動不可、留まるだけ。だが留まるは(0,0)で考慮済み
                    continue

        if found:
            print(ans_time, ans_r, ans_c)
        else:
            print("impossible")

if __name__ == "__main__":
    main()