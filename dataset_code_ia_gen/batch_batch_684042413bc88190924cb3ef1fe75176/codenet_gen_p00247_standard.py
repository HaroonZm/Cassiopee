from collections import deque

def solve():
    while True:
        X, Y = map(int, input().split())
        if X == 0 and Y == 0:
            break
        maze = [list(input()) for _ in range(Y)]

        # 探索用の方向ベクトル
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # 氷塊のグループ分け
        ice_id = [[-1]*X for _ in range(Y)]
        ice_groups = []
        gid = 0
        for y in range(Y):
            for x in range(X):
                if maze[y][x]=='X' and ice_id[y][x]==-1:
                    q = deque()
                    q.append((x,y))
                    ice_id[y][x] = gid
                    group = [(x,y)]
                    while q:
                        cx, cy = q.popleft()
                        for dx, dy in directions:
                            nx, ny = cx+dx, cy+dy
                            if 0<=nx<X and 0<=ny<Y:
                                if maze[ny][nx]=='X' and ice_id[ny][nx]==-1:
                                    ice_id[ny][nx] = gid
                                    q.append((nx, ny))
                                    group.append((nx, ny))
                    ice_groups.append(len(group))
                    gid += 1

        # S, Gの位置を探索
        for y in range(Y):
            for x in range(X):
                if maze[y][x]=='S':
                    sx, sy = x, y
                elif maze[y][x]=='G':
                    gx, gy = x, y

        max_ice_count = ice_groups

        # BFS 状態：(x,y, ice_visited各氷塊で通った回数のタプル)
        # ice通過回数は最大塊サイズの半分以下である必要がある
        # 状態のメモリ節約のため、氷塊がない場合を考慮
        ice_cnt = len(ice_groups)
        # 各氷塊の必要最大通過回数 (<= half)
        max_pass = [c//2 for c in ice_groups]

        from collections import deque

        # visited[(x,y, ice_counts)] = True
        # ice_countsは各氷塊の通過回数のタプル
        # 氷塊が無ければ空タプル
        init_ice_count = tuple([0]*ice_cnt)
        visited = set()
        visited.add((sx, sy, init_ice_count))
        q = deque()
        q.append((sx, sy, init_ice_count, 0))

        while q:
            x, y, ice_state, dist = q.popleft()
            if (x,y)==(gx,gy):
                print(dist)
                break
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<X and 0<=ny<Y:
                    c = maze[ny][nx]
                    if c=='#': # 山で通行不可
                        continue
                    # 新しい氷状態をコピー
                    new_ice_state = list(ice_state)
                    if c=='X':
                        i = ice_id[ny][nx]
                        # この氷塊の通過回数増分
                        ccount = new_ice_state[i]+1
                        if ccount > max_pass[i]:
                            continue # 氷割れで通れない
                        new_ice_state[i] = ccount
                    new_ice_state = tuple(new_ice_state)
                    if (nx, ny, new_ice_state) not in visited:
                        visited.add((nx, ny, new_ice_state))
                        q.append((nx, ny, new_ice_state, dist+1))

if __name__=="__main__":
    solve()