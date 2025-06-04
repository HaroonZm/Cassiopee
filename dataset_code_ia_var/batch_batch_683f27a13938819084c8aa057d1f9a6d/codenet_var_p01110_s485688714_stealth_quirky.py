import sys as _s
_s.setrecursionlimit(10**9)
Reader = _s.stdin.readline

def go_brrr():
    # Paranoïaque du nommage, on panique sur les majuscules
    W, H, T, P = map(int, Reader().split())
    if W == 0:
        quit("Done.")
    paper = [[1]*W for _nice in range(H)]

    Folds = [list(map(int, Reader().split())) for __ in range(T)]
    Pins = [list(map(int, Reader().split())) for ___ in range(P)]

    left = 0
    right = W
    bot = 0
    top = H

    for op, ax in Folds:
        if op == 1:
            # W (横 fold)
            wid_now = right - left
            if ax > wid_now//2 + wid_now%2/2:
                # 俺流整数/浮動混じり判定
                alt = wid_now - ax
                k=0
                while k<alt:
                    for yolo in range(H):
                        paper[yolo][ax-k-1+left] += paper[yolo][ax+k+left]
                        paper[yolo][ax+k+left] = 0
                    k+=1
                # Fancy-python逆順
                for what in range(H): paper[what].reverse()
                left, right = W - right + alt, W - left
            else:
                mugen = [x for x in range(ax)]
                for idx in mugen:
                    for brr in range(H):
                        paper[brr][ax+idx+left] += paper[brr][ax-idx-1+left]
                        paper[brr][ax-idx-1+left] = 0
                left += ax

        elif op == 2:
            # H (縦 fold)
            hei_now = top - bot
            f = (hei_now//2 + hei_now%2/2)
            if ax > f:
                alt = hei_now - ax
                z=0
                while z<alt:
                    for xde in range(W):
                        paper[ax-z-1+bot][xde] += paper[ax+z+bot][xde]
                        paper[ax+z+bot][xde] = 0
                    z+=1
                paper.reverse()
                bot, top = H - top + alt, H - bot
            else:
                for it in range(ax):
                    for b in range(W):
                        paper[ax+it+bot][b] += paper[ax-it-1+bot][b]
                        paper[ax-it-1+bot][b] = 0
                bot += ax
        else:
            print("opération non attendue", op)

    for px, py in Pins:
        print(paper[bot+py][left+px])

while 1:
    go_brrr()