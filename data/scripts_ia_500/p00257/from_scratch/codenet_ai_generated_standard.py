while True:
    max_roll = int(input())
    if max_roll == 0:
        break
    n = int(input())
    dice = [0] + [int(input()) for _ in range(n)] + [0]
    size = n + 2
    # next_pos[i][r] : pos after rolling r at i, then applying instruction once
    next_pos = [[0]*(max_roll+1) for _ in range(size)]
    for i in range(size):
        for r in range(1, max_roll+1):
            pos = i + r
            if pos >= size - 1:
                pos = size - 1
            else:
                pos2 = pos + dice[pos]
                if pos2 <= 0:
                    pos2 = 0
                elif pos2 >= size - 1:
                    pos2 = size - 1
                else:
                    # Only apply instruction once
                    pos2 = pos2
                pos = pos2
            next_pos[i][r] = pos
    from collections import deque
    visited = [False]*size
    can_reach = [False]*size
    can_reach[size-1] = True
    # Reverse BFS from goal to mark reachable positions
    for _ in range(size):
        updated = False
        for i in range(size):
            if can_reach[i]:
                continue
            for r in range(1, max_roll+1):
                if next_pos[i][r] < size and can_reach[next_pos[i][r]]:
                    can_reach[i] = True
                    updated = True
                    break
        if not updated:
            break
    # Check if start is reachable
    if not can_reach[0]:
        print("NG")
        continue
    # Detect cycle reachable from start
    color = [0]*size  # 0=white,1=gray,2=black
    res = "OK"
    def dfs(u):
        nonlocal res
        color[u] = 1
        for r in range(1,max_roll+1):
            v = next_pos[u][r]
            if v == size-1:
                continue
            if color[v] == 0:
                dfs(v)
                if res == "NG":
                    return
            elif color[v] == 1:
                # cycle detected
                # if cycle node is reachable to goal, skip
                if can_reach[v]:
                    continue
                res = "NG"
                return
        color[u] = 2
    dfs(0)
    print(res)