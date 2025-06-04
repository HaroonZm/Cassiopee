H_W = input().split()
while True:
    H, W = map(int, H_W)
    if H == 0:
        break
    if H * W % 2 == 1:
        print(0)
        H_W = input().split()
        continue
    state = [[-1]*W for _ in range(H)]
    k = 0
    stack = []
    stack.append((k, [row[:] for row in state]))
    res = 0
    while stack:
        k, state = stack.pop()
        if k == H * W:
            res += 1
            continue
        i, j = divmod(k, W)
        if state[i][j] != -1:
            stack.append((k+1, [row[:] for row in state]))
            continue
        cond = True
        if i > 0 and j > 0:
            a = state[i-1][j-1]
            b = state[i-1][j]
            c = state[i][j-1]
            if a != -1 and b != -1 and c != -1 and (a == b or b == c or c == a):
                cond = False
        if not cond:
            continue
        state1 = [row[:] for row in state]
        state1[i][j] = k
        if i+1 < H and state[i+1][j] == -1:
            state1b = [row[:] for row in state1]
            state1b[i+1][j] = k
            stack.append((k+1, state1b))
        if j+1 < W and state[i][j+1] == -1:
            state2 = [row[:] for row in state1]
            state2[i][j+1] = k
            stack.append((k+1, state2))
        # Option to move with just one
        # But original code always fills
    print(res)
    H_W = input().split()