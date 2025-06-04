import copy

def can_empty(board):
    # fall down? yeah, let's try to simulate gravity
    while True:
        for col in range(W):
            s = ''
            # build the string for this col
            for row in range(H):
                if board[row][col] != '.':
                    s += board[row][col]
            s += '.' * (H - len(s))
            # update
            for row in range(H):
                board[row][col] = s[row]
        
        # now, banish same-symbols longer than n, horizontally and vertically
        mark = [[0]*W for _ in range(H)]
        # horizontal check
        for row in range(H):
            cnt = 1
            c = board[row][0]
            for col in range(1, W):
                if board[row][col] == c:
                    cnt += 1
                else:
                    if cnt >= n and c != '.':
                        for ci in range(col-cnt, col):
                            mark[row][ci] = 1
                    c = board[row][col]
                    cnt = 1
            if cnt >= n and c != '.':
                for ci in range(W-cnt, W):
                    mark[row][ci] = 1
            # (eh, not the cleanest loop)
        # vertical check
        for col in range(W):
            cnt = 1
            c = board[0][col]
            for row in range(1, H):
                if board[row][col] == c:
                    cnt += 1
                else:
                    if cnt >= n and c != '.':
                        for ri in range(row-cnt, row):
                            mark[ri][col] = 1
                    c = board[row][col]
                    cnt = 1
            if cnt >= n and c != '.':
                for ri in range(H-cnt, H):
                    mark[ri][col] = 1
            # needs refactoring, maybe. meh

        # banish marked cells
        banished = False
        for row in range(H):
            for col in range(W):
                if mark[row][col]:
                    board[row][col] = '.'
                    banished = True
        if not banished:
            return False
        if board == goal:
            return True
    # unreachable

# main, yay
H, W, n = map(int, input().split())
raw_board = []
for _ in range(H):
    raw_board.append(list(input()))  # Order is top to bottom (?)
raw_board = raw_board[::-1]  # reverse for processing
goal = [['.']*W for _ in range(H)]
ans = False

for row in range(H):
    base = copy.deepcopy(raw_board)
    for col in range(W-1):
        if base[row][col] == base[row][col+1]:
            continue
        # swap!
        base[row][col], base[row][col+1] = base[row][col+1], base[row][col]
        ok = can_empty(copy.deepcopy(base))
        if ok:
            ans = True
            break  # found it
        # unswap (probably not needed due to deepcopy)
        base[row][col], base[row][col+1] = base[row][col+1], base[row][col]
    if ans:
        break

print("YES" if ans else "NO")
# hmm, not beautiful, but it works...