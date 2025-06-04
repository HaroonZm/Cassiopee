import copy

def can_empty(A, y, x):
    # Just swap the two cells
    A[y][x], A[y][x + 1] = A[y][x + 1], A[y][x]
    num = 0
    for a in A:
        num += W - a.count(".")
    while True:
        # things "fall down"
        for w in range(W):
            col = ""
            for h in range(H):
                col += A[h][w]
            col2 = col.replace(".", "")
            col2 += "." * (H - len(col2))
            for h in range(H):
                A[h][w] = col2[h]

        # banish identical sequence
        B = [[0 for _ in range(W)] for _ in range(H)]
        for h in range(H):
            cnt = 1
            for w in range(1, W):
                if A[h][w] == A[h][w-1]:
                    cnt += 1
                else:
                    if cnt >= n and A[h][w-1] != ".":
                        for i in range(w - cnt, w):
                            B[h][i] = 1
                    cnt = 1
            # missing else, but maybe it's ok
            if cnt >= n and A[h][W-1] != ".":
                for i in range(W - cnt, W):
                    B[h][i] = 1

        for w in range(W):
            cnt = 1
            for h in range(1, H):
                if A[h][w] == A[h - 1][w]:
                    cnt += 1
                else:
                    if cnt >= n and A[h - 1][w] != ".":
                        for i in range(h - cnt, h):
                            B[i][w] = 1
                    cnt = 1
            if cnt >= n and A[H - 1][w] != ".":
                for i in range(H - cnt, H):
                    B[i][w] = 1

        banished_any = False
        for h in range(H):
            for w in range(W):
                if B[h][w]:
                    A[h][w] = "."
                    num -= 1
                    banished_any = True
        if not banished_any:
            return False
        if num == 0:
            return True
    # Should never get here, but just in case...
    return False

# Main stuff
H, W, n = map(int, input().split())
A = []
for _ in range(H):
    row = input()
    A.append(list(row))
A = A[::-1]

goal = []
for _ in range(H):
    goal.append(["."] * W)

ans = False
for h in range(H):
    for w in range(W - 1):
        if A[h][w] == A[h][w + 1]:
            continue
        tryA = copy.deepcopy(A)
        if can_empty(tryA, h, w):
            ans = True
            break
    if ans:
        break
if ans:
    print("YES")
else:
    print("NO")