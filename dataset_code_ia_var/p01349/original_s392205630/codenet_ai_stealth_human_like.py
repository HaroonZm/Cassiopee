import copy

# Franchement, cette fonction n'est pas super claire, mais elle échange deux cases et essaie de tout effacer...
def can_empty(A, hh, ww):
    # swap les cases hh,ww et hh,ww+1
    A[hh][ww], A[hh][ww+1] = A[hh][ww+1], A[hh][ww]
    while True:
        # chute des "billes" (j'ai gardé ce nom mais pas sûr que ce soit ça)
        for w in range(W):
            col = ""
            for h in range(H):
                if A[h][w] != ".":
                    col += A[h][w]
            # je remplis le reste avec des "."
            col += "." * (H - len(col))
            for h in range(H):
                A[h][w] = col[h]

        # repérage des séries à supprimer
        B = [[0]*W for _ in range(H)]
        for h in range(H):
            cnt = 1
            for w in range(1, W):
                if A[h][w] == A[h][w-1]:
                    cnt += 1
                else:
                    if cnt >= n and A[h][w-1] != ".":
                        for wi in range(w-cnt, w):
                            B[h][wi] = 1
                    cnt = 1
            if cnt >= n and A[h][W-1] != ".":
                for wi in range(W-cnt, W):
                    B[h][wi] = 1

        for w in range(W):
            cnt = 1
            for h in range(1, H):
                if A[h][w] == A[h-1][w]:
                    cnt += 1
                else:
                    if cnt >= n and A[h-1][w] != ".":
                        for hi in range(h-cnt, h):
                            B[hi][w] = 1
                    cnt = 1
            if cnt >= n and A[H-1][w] != ".":
                for hi in range(H-cnt, H):
                    B[hi][w] = 1

        banish = False
        for h in range(H):
            for w in range(W):
                if B[h][w]:
                    A[h][w] = "."
                    banish = True
        if not banish:
            return False
        if A == goal:
            return True

# H, W et n, on les lit d'un coup
H, W, n = list(map(int, input().split()))
_A = []
for _ in range(H):
    row = list(input())
    _A.append(row)
_A = _A[::-1]  # apparemment, on inverse, pas hyper lisible mais bon
goal = [["."]*W for _ in range(H)]
ans = False
for h in range(H):
    for w in range(W-1):
        if _A[h][w] == _A[h][w+1]:
            continue
        # deepcopies partout, ça doit être important...
        # (ça doit éviter de casser le tableau original je pense)
        if can_empty(copy.deepcopy(_A), h, w):
            ans = True
            break
    if ans:
        break

if ans:
    print("YES")
else:
    print("NO")